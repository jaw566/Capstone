#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel
from UI.profileSelect import Ui_ProfileSelect
from UI.testCL import Ui_MainWindow

import subprocess
import socket 
import sys
import os
import signal
import time
import atexit
from klepto.archives import *
from functools import partial
import yaml

# globals
hostname = socket.gethostname()    
localIPAddress = socket.gethostbyname(hostname)
robotIPAddress = ""
ROSWorkspacePath = ""
radioBttns = []
configGroups = []
dependencies = {}
variables = []
versionNum = 0

class ImageDialog(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ImageDialog, self).__init__()
       
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Console.append("-------------------------------") 
        self.ui.Console.append("RosConnect Console") 
        self.ui.Console.append("-------------------------------") 

        # Remember to pass the definition/method, not the return value!


        # Load the config.yaml file to the Config window
        self.loadConfiguration()

        # Connect the buttons
        self.ui.StartCarBttn.clicked.connect(self.startCarBttnAction)
        self.ui.runSimBttn.clicked.connect(self.startSimBttnAction) 
        # self.ui.treeView.clicked.connect(self.populateEditor)

        # Connect the menu options
        self.ui.actionLoad_Profile.triggered.connect(lambda: self.loadProfile())
        self.ui.actionSave_Profile.triggered.connect(lambda: self.saveProfile())
    
    def loadConfiguration(self):
        # this is where the configuration file will be read in
        #  and radio buttons renamed
        with open('config.yaml') as file:
            modules = yaml.load(file, Loader=yaml.FullLoader)
            iteration = 0
            for module in modules.items():
                if(iteration == 0):
                    #iteration zero is our version number
                    global versionNum
                    versionNum = module[1]
                elif(iteration == 1):
                    #first group added to row 0 col 0
                    #makes a group for the current module
                    self.group = QtWidgets.QGroupBox(self.ui.centralwidget)
                    #sets the objects name to be the name module
                    self.group.setObjectName(module[1]["variable"]) 
                    self.ui.gridLayout.addWidget(self.group, 0, 0, 1, 3)
                    variables.append(module[1]["variable"])
                else:
                    #makes a group for the current module
                    self.group = QtWidgets.QGroupBox(self.ui.centralwidget)
                    #sets the objects name to be the name module
                    self.group.setObjectName(module[1]["variable"]) 
                    self.ui.gridLayout.addWidget(self.group, 1, \
                                                 iteration-2, 1, 1)
                    #all other groups added to row 1 and then the next open col
                    self.ui.gridLayout.addWidget(self.group, 1, iteration-2)
                    variables.append(module[1]["variable"])

                if(iteration >= 1):
                    self.group.setTitle(module[0]) #sets the title in the UI
                    #each group gets its own form layout that bttns are added to
                    self.formLayout = QtWidgets.QFormLayout(self.group)
                    self.formLayout.setObjectName("formLayout_" + module[0])
                    configGroups.append(list()) #makes array for the grouping
                    for choice in module[1]["choices"].items():
                        #print(choice[0]) var name of choice
                        #print(choice[1]["title"]) title of var seen in the GUI
                        radioBttns.append(choice[0]) # button array
                        # add buttons to their respective groups
                        configGroups[iteration-1].append(choice[0])
                        # create the button in the GUI
                        self.bttn = QtWidgets.QRadioButton(self.group)
                        #this is the name we use to access the object
                        self.bttn.setObjectName(choice[0]) 
                        #the text seen in the GUI
                        self.bttn.setText(choice[1]["title"]) 
                        #get this buttons dependency list
                        mydep = choice[1]["dependencies"]
                        dependencies[choice[0]] = mydep
                        #add the button to the layout
                        self.formLayout.addWidget(self.bttn) 
                        #connect onclicked function to the button
                        self.bttn.clicked.connect(partial(\
                            self.toggleOff,choice[0], iteration-1))
                        self.bttn.clicked.connect(partial(\
                            self.saveSelectedOptions,choice[0], iteration-1))
                        self.bttn.clicked.connect(partial(\
                            self.setDependencies,choice[0], mydep))
                iteration+=1
        # load any previously saved options in the klepto file savedData.txt
        self.loadPreviousOptions()        

    def toggleOff(self, this_radbttn, mod_num):
        cw = self.ui.centralwidget
        sz = len(configGroups[mod_num])
        count=0
        for choice in configGroups[mod_num]:
            radio_button = cw.findChild(QtWidgets.QRadioButton, choice)
            if radio_button.isChecked() == False:
                print(choice)
                count+=1
        if count == sz:
            # we are turning on the button
            for choice in configGroups[mod_num]:
                radio_button = cw.findChild(QtWidgets.QRadioButton, choice)
                if radio_button.isEnabled():
                    radio_button.setChecked(True)
        else:
            for choice in configGroups[mod_num]:
                radio_button = cw.findChild(QtWidgets.QRadioButton, choice)
                radio_button.setAutoExclusive(False) 
            for choice in configGroups[mod_num]:
                print(choice)
                radio_button = cw.findChild(QtWidgets.QRadioButton, choice)
                radio_button.setChecked(False)
        
    def setDependencies(self, this_radbttn, dependencies):
        if dependencies != None:
            cw = self.ui.centralwidget
            sz = len(configGroups)
            for i in range(0, sz):
                group = configGroups[i]
                for choice in group:
                    if(choice != this_radbttn) and (choice not in dependencies):
                        radio_button=cw.findChild(QtWidgets.QRadioButton,choice)
                        radio_button.setEnabled(False)

    def saveSelectedOptions(self, name, moduleNum):
        arch = file_archive('savedData.txt', serialized=True)
        mapp = arch.archive
        arch["Version"] = versionNum
        group = configGroups[moduleNum]
        for choice in group:
            if choice in mapp:
                mapp.pop(choice)
        arch[variables[moduleNum]] = name
        arch.dump()

    def loadData(self, dictionary, from_savedData):
        if( from_savedData ):
            self.ui.Console.append("> ...")
            self.ui.Console.append("> Loading previous session")
    
            if len(dictionary) == 0: #if empty dictionary
                self.ui.Console.append("> WARNING: saved session not found.")
                self.ui.Console.append(">          The config window will be") 
                self.ui.Console.append(">          left blank.")
                #self.ui.Console.append("> Select 'Load File' from File")
                #self.ui.Console.append("> drop-down menu to load a profile")
                #self.ui.Console.append("> ...")
                #self.ui.Console.append("> OR ")
                #self.ui.Console.append("> ...")
                #self.ui.Console.append("> Make appropriate selections in the")
                #self.ui.Console.append("> configuration window. Then select")
                #self.ui.Console.append("> 'Save Profile' from the drop-down")
                #self.ui.Console.append("> menu to save your profile")
                return

            elif "Version:" in dictionary:
                 if dictionary["Version:"] != str(versionNum):
                    self.ui.Console.append("> WARNING: Config Version Mismatch.\
                                              Could not load previous session.")
                    return
            elif dictionary["Version"] != versionNum : #if version doesn't match
                self.ui.Console.append("> WARNING: Config Version Mismatch. \
                                           Could not load previous session.")
                return

            cw = self.ui.centralwidget
            iteration = 0
            for i in dictionary:
                if iteration != 0:
                    var=cw.findChild(QtWidgets.QRadioButton, dictionary[i])
                    var.toggle()
                iteration+=1  
            self.ui.Console.append("> Previous session successfully loaded.")


        else:
            self.ui.Console.append("> ...")
            self.ui.Console.append("> Loading profile")
    
            if len(dictionary) == 0: #if empty dictionary
                self.ui.Console.append("> WARNING: profile is blank.")
                return

            elif "Version:" in dictionary:
                 if dictionary["Version:"] != str(versionNum):
                    self.ui.Console.append("> WARNING: Config Version Mismatch.\
                                              Could not load profile.")
                    return
            elif dictionary["Version"] != versionNum : #if version doesn't match
                self.ui.Console.append("> WARNING: Config Version Mismatch.\
                                           Could not load profile.")
                return

            cw = self.ui.centralwidget
            #print(dictionary)
            iteration = 0
            for i in dictionary:
                if iteration != 0:
                   # print(dictionary[i])
                    var=cw.findChild(QtWidgets.QRadioButton, dictionary[i])
                    var.toggle()
                iteration+=1  
            self.ui.Console.append("> Your selected profile has been")
            self.ui.Console.append("> successfully loaded.")
        

    def loadPreviousOptions(self):
        arch = file_archive('savedData.txt')
        dictionary = arch.archive
        self.loadData(dictionary,True)

        # make sure to disable any buttons not in dependency tree
        cw = self.ui.centralwidget
        sz = len(configGroups)
        for i in range(0, sz):
            for choice in configGroups[i]:
                radio_button = cw.findChild(QtWidgets.QRadioButton, choice)
                if( radio_button.isChecked() ):
                    self.setDependencies(choice, dependencies[choice]) 
                    return

    def generateLaunchVars(self):
        arch = file_archive('savedData.txt')
        dictionary = arch.archive
        param = ""
        for i in dictionary:
            if i == 'Version':
                continue

            test = i +":=" +  dictionary[i]
            param += test + " "
        return param
        #command = 'cd Scripts; ./runLaunch.sh "$1"'
        #subprocess.call([command, 'sh',param], shell=True)
        
    def startCarBttnAction(self):
        # define global bool value for use at closure of application
        global CAR_RUNNING
        self.ui.Console.append("> ...")
        self.ui.Console.append("> Starting car")
        self.ui.Console.append("> This may take some time")
        params = self.generateLaunchVars()
        command = 'cd Scripts; ./runSSH.sh "$1"'
        runcar = subprocess.call([command, 'sh',params], shell=True)
        #subprocess.call(['Scripts/./runSSH.sh >> kpw_logFile.txt'], shell=True)

    def startSimBttnAction(self):
        self.ui.Console.append("> ...")
        self.ui.Console.append("> Loading simulator")
        global SIM_RUNNING
        SIM_RUNNING = subprocess.Popen(['cd Scripts; screen -dmS sim \
                            ./runSim.sh &'], shell=True, preexec_fn=os.setsid) 
        if SIM_RUNNING.returncode == None:
            self.ui.Console.append("> Simulator has been loaded successfully")
        else:
            self.ui.Console.append("> Error: simulator has *not* been loaded")
            
    def emergencyBttnAction(self):
        # This is executed when the button is pressed
        self.ui.Console.append("> ...")
        self.ui.Console.append("> Stopping car")
        self.ui.Console.append("> This may take some time")
        subprocess.call(['./stopCar.py'])

    def loadProfile(self):
        dictionary = {}
        dialog = QFileDialog()
        fname = dialog.getOpenFileName(None, ("Select File"), ".txt")
        with open(fname[0]) as file:
            #do stuff with the file
            for index in file: 
                (key, val) = index.split()
                dictionary[key] = val
        self.loadData(dictionary,False)

    def saveProfile(self):
        self.ui.Console.append("> ...")
        self.ui.Console.append("> Saving profile")

        name = QFileDialog.getSaveFileName(self, 'Save File')
        f = open(name[0],'w')
        arch = file_archive('savedData.txt')
        dictionary = arch.archive
        for i in dictionary:
            f.write("%s: %s\n" % (i,dictionary[i]))
        f.close()
        self.ui.Console.append("> Your profile has been saved sucessfully.")

    @atexit.register
    def closeROS():
        # print("Begin killing program...")
        nodes = os.popen("rosnode list").readlines()
        for i in range(len(nodes)):
            nodes[i] = nodes[i].replace("\n","")
        for node in nodes:
            os.system("rosnode kill "+ node)
        if( 'SIM_RUNNING' in globals() ):
            os.system("screen -S sim -X quit")
        if( 'CAR_RUNNING' in globals() ):
            subprocess.call(['Scripts/./closeScreen.sh >> kpw_logFile.txt'], \
                                                                    shell=True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ImageDialog()
    #ui.setupUi(window)
    ui.show()
    #ui.openProfileLoader()
    sys.exit(app.exec_())
    



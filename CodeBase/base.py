#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel
from UI.profileSelect import Ui_ProfileSelect
from UI.testCL import Ui_MainWindow
from klepto.archives import *
from functools import partial

import subprocess
import socket 
import sys
import os
import signal
import time
import atexit
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


        # Create globle variable for cw
        global cw
        cw = self.ui.centralwidget

        # Remember to pass the definition/method, not the return value!

        # Load the config.yaml file to the Config window
        self.loadConfiguration()

        # Show mouse over 
        self.showHelp()

        # Connect the buttons
        self.ui.StartCarBttn.clicked.connect(self.startCarBttnAction)
        self.ui.runSimBttn.clicked.connect(self.startSimBttnAction)
        self.ui.stopCarBttn.clicked.connect(self.emergencyBttnAction)
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
                    # iteration zero is our version number
                    global versionNum
                    versionNum = module[1]
                elif(iteration == 1):
                    # first group added to row 0 col 0
                    # makes a group for the current module
                    self.group = QtWidgets.QGroupBox(self.ui.centralwidget)
                    # sets the objects name to be the name module
                    self.group.setObjectName(module[1]["variable"]) 
                    self.ui.gridLayout.addWidget(self.group, 0, 0, 1, 3)
                    variables.append(module[1]["variable"])
                else:
                    # makes a group for the current module
                    self.group = QtWidgets.QGroupBox(self.ui.centralwidget)
                    # sets the objects name to be the name module
                    self.group.setObjectName(module[1]["variable"]) 
                    self.ui.gridLayout.addWidget(self.group, 1, \
                                                 iteration-2, 1, 1)
                    # all other groups added to row 1 and then the next open col
                    self.ui.gridLayout.addWidget(self.group, 1, iteration-2)
                    variables.append(module[1]["variable"])

                if(iteration >= 1):
                    self.group.setTitle(module[0]) # sets the title in the UI
                    self.group.setToolTip('This is a module part of the configuration.')
                    # each group gets its own form layout where bttns are added
                    self.formLayout = QtWidgets.QFormLayout(self.group)
                    self.formLayout.setObjectName("formLayout_" + module[0])
                    configGroups.append( list() ) # makes array for the grouping
                    for choice in module[1]["choices"].items():
                        radioBttns.append(choice[0]) # button array
                        # add buttons to their respective groups
                        configGroups[iteration-1].append(choice[0])
                        # create the button in the GUI
                        self.bttn = QtWidgets.QRadioButton(self.group)
                        # this is the name we use to access the object
                        self.bttn.setObjectName(choice[0]) 
                        # Set the tool tip/mouse over for help. 
                        self.bttn.setToolTip('This is a valid option for a configuration.')
                        # the text seen in the GUI
                        self.bttn.setText(choice[1]["title"]) 
                        # get this buttons dependency list
                        mydep = choice[1]["dependencies"]
                        # save the dependency list from yaml to global variable
                        dependencies[choice[0]] = mydep
                        # add the button to the layout
                        self.formLayout.addWidget(self.bttn) 
                        # connect onclicked function to the button
                        self.bttn.clicked.connect(partial(\
                            self.saveSelectedOptions,choice[0], iteration-1))
                        self.bttn.clicked.connect(partial(\
                            self.setDependencies,choice[0], mydep))
                iteration+=1
        # load any previously saved options in the klepto file savedData.txt
        self.loadPreviousOptions()        

    def setDependencies(self, this_radbttn, dependencies):
        sz = len(configGroups)
        for i in range(0, sz): # loop over all groups
            group = configGroups[i]
            if dependencies != None: # do we have a depenedencies list?
                for choice in group: 
                    if(choice != this_radbttn) and (choice not in dependencies):
                        radio_button=cw.findChild(QtWidgets.QRadioButton,choice)
                        radio_button.setEnabled(False)
                        radio_button.setAutoExclusive(False)
                        if radio_button.isChecked():
                            radio_button.toggle()
                        radio_button.setToolTip('This is a dependency and can not be selected.')
                    else:
                        radio_button=cw.findChild(QtWidgets.QRadioButton,choice)
                        radio_button.setAutoExclusive(False)
                radio_button.setToolTip('This is a dependency and can not be selected.')
            else: # otherwise, assume we have no dependencies for this button
                for choice in group: 
                    radio_button=cw.findChild(QtWidgets.QRadioButton,choice)
                    radio_button.setAutoExclusive(False)
                    radio_button.setToolTip('All options may be selected. No dependencies.')
        # determine if all the buttons are un-clicked
        enable_all = True
        for i in range(0, sz): # loop over all groups
            group = configGroups[i]
            for choice in group:
                radio_button=cw.findChild(QtWidgets.QRadioButton,choice)
                if radio_button.isChecked():
                    enable_all = False
        # if so, then undo all disabling
        if enable_all:
            for i in range(0, sz): # loop over all groups
                group = configGroups[i]
                for choice in group:
                    radio_button=cw.findChild(QtWidgets.QRadioButton,choice)
                    radio_button.setEnabled(True)

    def saveSelectedOptions(self, name, moduleNum):
        arch = file_archive('savedData.txt', serialized=True)
        mapp = arch.archive
        arch["Version"] = versionNum
        # this radio buttons group
        group = configGroups[moduleNum]
        # find our radio button object
        for choice in group:
            if choice == name:
                radio_button=cw.findChild(QtWidgets.QRadioButton,choice)
                break
        # if the button is checked, then add it to the savedData.txt file
        if radio_button.isChecked():
            arch[variables[moduleNum]] = name
            arch.dump()
        else: # otherwise remove the button from savedData.txt
            mapp.pop(variables[moduleNum])

    def showHelp(self):
        self.ui.StartCarBttn.setToolTip('Select the configuration you want then press start car to start the car.')
        self.ui.runSimBttn.setToolTip('Select the configuration you want. Press run sim to see how the car will perform in a simulation.')
        self.ui.stopCarBttn.setToolTip('Press Stop car and have a script sent to the car to stop it.')
        self.ui.Console.setToolTip('This is where we will show important information to the user.')
        self.ui.menubar.setToolTip('Inside the file you will see a load and save profile option.')
        self.ui.menuFile.setToolTip('The load profile takes in a saved profile and loads it into the GUI.\nThe save profile will take current selected configurations and save them to a file.')
        self.ui.actionLoad_Profile.setToolTip('This is where you can select a profile to load into the GUI.')  
        self.ui.actionLoad_Profile.setToolTip('This is where you can save the selected configuration to a window.')

    def loadData(self, dictionary, from_savedData):
        # Print where we are loading data from. 
        if( from_savedData ):
            self.ui.Console.append("> ...")
            self.ui.Console.append("> Loading previous session")

        else:
            self.ui.Console.append("> ...")
            self.ui.Console.append("> Loading profile")

        # Check to see if dictionary is empty
        # Depending on where we are loading from gives a different message. 
        if len(dictionary) == 0:
            if from_savedData:
                self.ui.Console.append("> WARNING: saved session not found.")
                self.ui.Console.append(">          The config window will be")
                self.ui.Console.append(">          left blank.")
                return
            else:
                self.ui.Console.append("> WARNING: profile is blank.")
                return

        # Check to see if version numbers match 
        if "Version:" in dictionary:
            if dictionary["Version"] != str(versionNum):
                if from_savedData:
                    self.ui.Console.append("> WARNING: Config Version Mismatch. Could not load previous session.")
                else:
                    print("Inside comparison of version numbers")
                    self.ui.Console.append("> WARNING: Config Version Mismatch. Could not load profile.")

        # Check to see if we are loading from a file. 
        if (not from_savedData):
            # - Clear the config window of any settings
            sz = len(configGroups)
            #   - enabled all buttons
            #   - un toggle all buttons that are currently toggled
            for i in range(0, sz):
                for choice in configGroups[i]:
                    radio_button = cw.findChild(QtWidgets.QRadioButton, choice)
                    radio_button.setEnabled(True)
                    if radio_button.isChecked():
                        radio_button.toggle()

        # Load data into the GUI
        iteration = 0
        for i in dictionary:
            if iteration != 0:
                var=cw.findChild(QtWidgets.QRadioButton, dictionary[i])
                if var is not None:
                    var.toggle()
                else:
                    self.ui.Console.append("> You are not able to toggle a radio button that doesn't exist.")

            iteration+=1
        # make sure to disable any buttons not in this dependency tree
        sz = len(configGroups)
        for i in range(0, sz):
            for choice in configGroups[i]:
                radio_button = cw.findChild(QtWidgets.QRadioButton, choice)
                if( radio_button.isChecked() ):
                    self.setDependencies(choice, dependencies[choice])
                    if from_savedData:
                        self.ui.Console.append("> Previous session successfully loaded.")
                    else:
                        self.ui.Console.append(">  Your selected profile has been successfully loaded")
                    return

    def loadPreviousOptions(self):
        arch = file_archive('savedData.txt')
        dictionary = arch.archive
        self.loadData(dictionary,True)

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
        self.ui.Console.append(">  This may take some time")
        params = self.generateLaunchVars()
        command = 'cd Scripts; ./runSSH.sh "$1"'
        CAR_RUNNING = subprocess.Popen([command, 'sh',params], \
                                        shell=True, preexec_fn=os.setsid)
        if CAR_RUNNING.returncode == None:
            self.ui.Console.append("> Vehicle has been loaded successfully")
        else:
            self.ui.Console.append("> Error: Vehicle has *not* been loaded")

    def startSimBttnAction(self):
        self.ui.Console.append("> ...")
        self.ui.Console.append("> Loading simulator")
        global SIM_RUNNING
        arch = file_archive('savedData.txt')
        dictionary = arch.archive
        simVar = dictionary['strat']

        if (simVar == "Racing_2"):
            SIM_RUNNING = subprocess.Popen(['cd Scripts; screen -dmS sim \
                        ./runSimWall.sh &'], shell=True, preexec_fn=os.setsid)
                
        elif (simVar == "Racing_3"):
            SIM_RUNNING = subprocess.Popen(['cd Scripts; screen -dmS sim \
                        ./runSimKB.sh &'], shell=True, preexec_fn=os.setsid)

        else:
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
        self.ui.Console.append(">  This may take some time")
        subprocess.call(['cd Scripts; ./carStop.sh'], shell=True)

    def loadProfile(self):
        dictionary = {}
        dialog = QFileDialog()
        fname = dialog.getOpenFileName(None, ("Select File"), ".txt")
        arch = file_archive('savedData.txt')
        disk = arch.archive
        # clear the disk archive
        for key in disk:
            if "Version" not in key:
                disk.pop(key)
       # print(disk)
        with open(fname[0]) as file:
            for index in file: 
                (key, val) = index.split()
                key = key[:len(key) -1 ]
                if val in radioBttns or key == "Version":
                    dictionary[key] = val                
                else:
                    self.ui.Console.append("> The value for {} is not part of the current config file".format(key))
                arch[key] = val
        arch.dump()
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
        self.ui.Console.append(">  Your profile has been saved sucessfully.")

    @atexit.register
    def closeROS():
        nodes = os.popen("rosnode list").readlines()
        for i in range(len(nodes)):
            nodes[i] = nodes[i].replace("\n","")
        for node in nodes:
            os.system("rosnode kill "+ node)
        if( 'SIM_RUNNING' in globals() ):
            os.system("screen -S sim -X quit")
        if( 'CAR_RUNNING' in globals() ):
            subprocess.call(['cd Scripts; ./closeScreen.sh'], shell=True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ImageDialog()
    #ui.setupUi(window)
    ui.show()
    #ui.openProfileLoader()
    sys.exit(app.exec_())
    



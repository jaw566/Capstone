#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel
import sys

from UI.profileSelect import Ui_ProfileSelect
from UI.testCL import Ui_MainWindow

import subprocess
import socket 
import os
import signal

# JAW - closure of ROS
import atexit
# JAW - saving config window session
from klepto.archives import *
from functools import partial

import yaml

#variables
hostname = socket.gethostname()    
localIPAddress = socket.gethostbyname(hostname)
robotIPAddress = ""
ROSWorkspacePath = ""
radioBttns = []
configGroups = []
variables = []
versionNum = 0
param = ""
running = True

class ImageDialog(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ImageDialog, self).__init__()
       
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

         # JAW - console code
        # hard coded text in console      
        self.ui.Console.append("Starting RosLaunch Console") 
        self.ui.Console.append("=======================") 
        #self.ui.Console.append("ROS core INITIATED...........") 
        self.ui.Console.append("Simulator READY.............")
        # Remember to pass the definition/method, not the return value!

        # Make local modifications.
        self.loadConfiguration()
        # Connect up the buttons.
        self.ui.StartCarBttn.clicked.connect(self.startCarBttnAction)
        self.ui.runSimBttn.clicked.connect(self.startSimBttnAction) 
        #self.ui.runSimBttn.clicked.connect(self.logContentsFromFile)
        #self.ui.treeView.clicked.connect(self.populateEditor)

        # Connect up the menu options
        self.ui.actionLoad_Profile.triggered.connect(lambda: self.loadProfile())
        self.ui.actionSave_Profile.triggered.connect(lambda: self.saveProfile())
      
       

        
    def loadConfiguration(self):
        #this is where the config fill will be read in and radio buttons remnamed
        with open('config.yaml') as file:
            modules = yaml.load(file, Loader=yaml.FullLoader)
            iteration = 0
            for module in modules.items():
                #print(modules)
                
                if(iteration == 0):
                    #iteration zero is our version number
                    #print(module[1])
                    global versionNum
                    versionNum = module[1]

                elif(iteration == 1):
                    #first group added to row 0 col 0
                    #makes a group for the currebnt module
                    self.group = QtWidgets.QGroupBox(self.ui.centralwidget)
                    self.group.setObjectName(module[1]["variable"]) #sets the objects name to be the name module
                    self.ui.gridLayout.addWidget(self.group, 0, 0, 1, 3)
                    variables.append(module[1]["variable"])
                else:
                    #makes a group for the currebnt module
                    self.group = QtWidgets.QGroupBox(self.ui.centralwidget)
                    self.group.setObjectName(module[1]["variable"]) #sets the objects name to be the name module
                    self.ui.gridLayout.addWidget(self.group, 1, iteration-2, 1, 1)
                    #all other groups added to row 1 and then the next open col
                    self.ui.gridLayout.addWidget(self.group, 1, iteration-2)
                    variables.append(module[1]["variable"])

                if(iteration >= 1):
                    self.group.setTitle(module[0]) #sets the title in the UI
                        
                    #each group gets its own form layout that the bttns are added to
                    self.formLayout = QtWidgets.QFormLayout(self.group)
                    self.formLayout.setObjectName("formLayout_" + module[0])
                        
                    #print(module)
                    configGroups.append(list()) #makes the array for the groupping
                
                    for choice in module[1]["choices"].items():
                        #print(choice[0]) var name of choice
                        #print(choice[1]["title"]) title of var thats seen in the GUI
                        radioBttns.append(choice[0]) # an array to keep track of the bttns
                        configGroups[iteration-1].append(choice[0]) #add bttns to thier groups
                        #create the button
                        self.bttn = QtWidgets.QRadioButton(self.group)
                        self.bttn.setObjectName(choice[0]) #this is the name we use to access the object
                        self.bttn.setText(choice[1]["title"]) #the text seen in the GUI
                        self.formLayout.addWidget(self.bttn) #add the button to the layout
                        #connect onclicked function to the button
                        self.bttn.clicked.connect(partial(self.saveSelectedOptions,choice[0], iteration-1))
                iteration+=1
        #test arrays
        #print(configGroups)
        #print(radioBttns)
        self.loadPreviousOptions()

    def saveSelectedOptions(self, name, moduleNum):
        arch = file_archive('savedData.txt', serialized=True)
        mapp = arch.archive
        arch["Version"] = versionNum
        group = configGroups[moduleNum]

        for choice in group:
            #print(choice)
            if choice in mapp:
                mapp.pop(choice)
                #arch.pop(choice)
        arch[variables[moduleNum]] = name
        arch.dump()
        #print(arch.archive)

    def loadData(self, dictionary):
         if len(dictionary) == 0: #if empty dictionary
             self.ui.Console.append("No previous profile found.")
             return
         elif "Version:" in dictionary:
              if dictionary["Version:"] != str(versionNum):
                 self.ui.Console.append("Config Version Mismatch. Could not load previous profile.")
                 return
         elif dictionary["Version"] != versionNum : #if version doesn't match
             self.ui.Console.append("Config Version Mismatch. Could not load previous profile.")
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

    def loadPreviousOptions(self):
        arch = file_archive('savedData.txt')
        dictionary = arch.archive
        print(dictionary)
        self.loadData(dictionary)


    def generateLaunchVars(self):
        arch = file_archive('savedData.txt')
        dictionary = arch.archive
        global param 
        param = ""
        for i in dictionary:
            if i == 'Version':
                continue

            test = i +":=" +  dictionary[i]
            param += test + " "
        #command = 'cd Scripts; ./runLaunch.sh "$1"'
        #subprocess.call([command, 'sh',param], shell=True)
        
    def startCarBttnAction(self):
        # This is executed when the button is pressed
        self.ui.Console.append("Starting Car....")
        self.generateLaunchVars()
        command = 'cd Scripts; ./runSSH.sh "$1"'
        subprocess.call([command, 'sh',param], shell=True)
        #subprocess.call(['Scripts/./runSSH.sh >> kpw_logFile.txt'], shell=True)



    def startSimBttnAction(self):
        # This is executed when the button is pressed
        #print('Run Sim Button Pressed')
        self.ui.Console.append("Simulator RUNNING....")
        global proc_sim
       # proc_sim = subprocess.Popen(['cd Scripts; screen -dmS jaw ./runSim.sh &'], \
       #                                     shell=True,preexec_fn=os.setsid)        

    def emergencyBttnAction(self):
        # This is executed when the button is pressed
        self.ui.Console.append("Stop the Car....")
       #subprocess.call(['./stopCar.py'])

    def logContentsFromFile(self):
        curr_wkg_dir = os.getcwd()
        myfile = QtCore.QFile(curr_wkg_dir+"/logfile_sim.txt")
        myfile.open(QtCore.QIODevice.ReadOnly)
        stream = QtCore.QTextStream(myfile)
        content = stream.read(200)
        self.ui.Console.append("Logging Contents from Simulation")
        self.ui.Console.append("================================")
        # TODO: read one line at a time and translate
        myfile.close()
        self.ui.Console.append(content)

    def loadProfile(self):
        dictionary = {}
        dialog = QFileDialog()
        fname = dialog.getOpenFileName(None, ("Select File"), ".txt") #returns string
        #print(fname)
        with open(fname[0]) as file:
            #do stuff with the file
            for index in file: 
                (key, val) = index.split()
                dictionary[key] = val

        print(dictionary)
        self.loadData(dictionary)
        self.ui.Console.append("Your profile has been loaded sucessfully. ")

    def saveProfile(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        f = open(name[0],'w')
        arch = file_archive('savedData.txt')
        diction = arch.archive
        dictionary = {}

        for index in arch.archive:
            #print(index)
            #print(dictionary[index])
            dictionary[index] = diction[index]
            #print(diction)
        print(yaml.dump(dictionary,default_flow_style=False))
        f.write(yaml.dump(dictionary))
        f.close()

    # JAW - closure of ROS
    @atexit.register
    def closeROS():
        print("Begin killing program...")
        nodes = os.popen("rosnode list").readlines()
        for i in range(len(nodes)):
            nodes[i] = nodes[i].replace("\n","")
        for node in nodes:
            os.system("rosnode kill "+ node)
        if( 'proc_sim' in globals()):
            os.system("screen -S jaw -X quit")
        if( 'proc_roscore' in globals()):
            os.killpg(proc_roscore.pid,signal.SIGTERM)

    # KPW - Begin closing of screen
    @atexit.register
    def closeScreen():
        print("Begin killing screen on car")
        #subprocess.call(['Scripts/./closeScreen.sh >> kpw_logFile.txt'], shell=True)

if __name__ == "__main__":
#    proc_roscore=subprocess.Popen(['roscore &'],shell=True,preexec_fn=os.setsid)
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ImageDialog()
    #ui.setupUi(window)
    ui.show()
    #ui.openProfileLoader()
    sys.exit(app.exec_())
    



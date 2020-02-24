#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel
import sys

from profileSelect import Ui_ProfileSelect
from clientUINoBttns import Ui_MainWindow

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
proc_sim=0
radioBttns = []
configGroups = []

class ImageDialog(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ImageDialog, self).__init__()
       
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Make local modifications.
        self.loadConfiguration()
        # Connect up the buttons.
        self.ui.StartCarBttn.clicked.connect(self.startCarBttnAction)
        self.ui.runSimBttn.clicked.connect(self.startSimBttnAction) 
        self.ui.runSimBttn.clicked.connect(self.logContentsFromFile)
        #self.ui.treeView.clicked.connect(self.populateEditor)

        # Connect up the menu options
        self.ui.actionSelect_Profile.triggered.connect(lambda: self.openProfileLoader())
      
        # JAW - console code
        # hard coded text in console      
        self.ui.Console.append("Starting RosLaunch Console") 
        self.ui.Console.append("=======================") 
        #self.ui.Console.append("ROS core INITIATED...........") 
        self.ui.Console.append("Simulator READY.............")
        # Remember to pass the definition/method, not the return value!

        
    def loadConfiguration(self):
        #this is where the config fill will be read in and radio buttons remnamed
        with open('config.yaml') as file:
            modules = yaml.load(file, Loader=yaml.FullLoader)
            iteration = 0
            rank_in_grp=0
            for module in modules.items():
                #print(module, ':', packages)
                #makes a group for the currebnt module
                self.group = QtWidgets.QGroupBox(self.ui.centralwidget)
                self.group.setObjectName(module[1]["variable"]) #sets the objects name to be the name module
                
                if(iteration == 0):
                    #first group added to row 0 col 0
                    self.ui.gridLayout.addWidget(self.group, 0, 0)
                else:
                    #all other groups added to row 1 and then the next open col
                    self.ui.gridLayout.addWidget(self.group, 1, iteration-1)

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
                    configGroups[iteration].append(choice[0]) #add bttns to thier groups
                    #create the button
                    self.bttn = QtWidgets.QRadioButton(self.group)
                    self.bttn.setObjectName(choice[0]) #this is the name we use to access the object
                    self.bttn.setText(choice[1]["title"]) #the text seen in the GUI
                    self.formLayout.addWidget(self.bttn) #add the button to the layout
                    #connect onclicked function to the button
                    self.bttn.clicked.connect(partial(self.saveSelectedOptions,choice[0],iteration,rank_in_grp))
                    rank_in_grp+=1
                iteration+=1
        #test arrays
        print(configGroups)
        print(radioBttns)
        self.loadPreviousOptions()

    def saveSelectedOptions(self, name, iteration, rank):
        tmp='button'
        arch = file_archive('savedData.txt', serialized=True)
        print(name)
        mapp = arch.archive
        if rank==1 or rank==4 or rank==7 or rank==10:
            if tmp+str(rank+1) in mapp:
                mapp.pop(tmp+str(rank+1))
            if tmp+str(rank-1) in mapp:
                mapp.pop(tmp+str(rank-1))
        elif rank==0 or rank==3 or rank==6 or rank==9:
            if tmp+str(rank+1) in mapp:
                mapp.pop(tmp+str(rank+1))
            if tmp+str(rank+2) in mapp:
                mapp.pop(tmp+str(rank+2))
        else:
            if tmp+str(rank-1) in mapp:
                mapp.pop(tmp+str(rank-1))
            if tmp+str(rank-2) in mapp:
                mapp.pop(tmp+str(rank-2))
        arch[name] = 'y'
        arch.dump()
        print(mapp)

    def loadPreviousOptions(self):
        arch = file_archive('savedData.txt')
        dictionary = arch.archive
        cw = self.ui.centralwidget
        print(dictionary)
        for i in dictionary:
            if dictionary[i] == 'y':
                print(i)
                var=cw.findChild(QtWidgets.QRadioButton, i)
                var.toggle()

        
    def startCarBttnAction(self):
        # This is executed when the button is pressed
        self.ui.Console.append("Starting Car....")
        subprocess.call(['Scripts/./runCar.sh >> &'], shell=True)

    def startSimBttnAction(self):
        # This is executed when the button is pressed
        #print('Run Sim Button Pressed')
        self.ui.Console.append("Simulator RUNNING....")
        os.system('Scripts/./runSim.sh >> logfile_sim.txt &')
        #print(proc_sim)
        #proc_sim = subprocess.Popen(['scripts/./runSim.sh >> logfile_sim.txt &',ROSWorkspacePath],shell=True,preexec_fn=os.setsid)

    def emergencyBttnAction(self):
        # This is executed when the button is pressed
        self.ui.Console.append("Stop the Car....")
        subprocess.call(['./stopCar.py'])

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

    def createProfile(self):
        robotIPAddress = self.ui.robotIPLabel.text
        ROSWorkspacePath = self.ui.ROSWSField.text
        self.window.close()

    def openProfileLoader(self):
        self.profile_window = QtWidgets.QMainWindow()
        self.profile_ui = Ui_ProfileSelect()
        self.profile_ui.setupUi(self.profile_window)
        
        self.profile_ui.localIPAddressField.setText(localIPAddress)
        self.profile_ui.browseROSWSBttn.clicked.connect(self.filePicker)
        self.profile_ui.createProfileBttn.clicked.connect(self.createProfile)
        self.profile_window.show()

    def filePicker(self):
        dialog = QFileDialog()
        fname = dialog.getExistingDirectory(None, ("Select Folder")) #returns string
        ROSWorkspacePath = "~" + fname
        self.profile_ui.ROSWSField.setText(fname) #element 0 is our file path
        # print(ROSWorkspacePath)
        self.model = QFileSystemModel()
        self.model.setRootPath(ROSWorkspacePath)
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index(QtCore.QDir.currentPath()))
        

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
    



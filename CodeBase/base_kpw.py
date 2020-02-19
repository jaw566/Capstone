#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel
import sys

from profileSelect import Ui_ProfileSelect
from clientUI import Ui_MainWindow

import subprocess
import socket 
import os
import signal

# JAW - closure of ROS
import atexit
# JAW - saving config window session
from klepto.archives import *
from functools import partial
import configparser

#variables
hostname = socket.gethostname()    
localIPAddress = socket.gethostbyname(hostname)
robotIPAddress = ""
ROSWorkspacePath = ""
radioBttns = ["radioButton_0", "radioButton_1", "radioButton_2",
              "radioButton_3", "radioButton_4", "radioButton_5", 
              "radioButton_6", "radioButton_7", "radioButton_8", 
              "radioButton_9", "radioButton_10","radioButton_11"]

class ImageDialog(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ImageDialog, self).__init__()
       
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Make local modifications.
        #self.loadOptions()

        # Connect up the buttons.
        self.ui.StartCarBttn.clicked.connect(self.startCarBttnAction)
        self.ui.runSimBttn.clicked.connect(self.startSimBttnAction) 
        self.ui.runSimBttn.clicked.connect(self.logContentsFromFile)
        self.ui.stopCarBttn.clicked.connect(self.emergencyBttnAction)
        #self.ui.treeView.clicked.connect(self.populateEditor)

        self.ui.radioButton_0.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[0],0))
        self.ui.radioButton_1.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[1],1))
        self.ui.radioButton_2.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[2],2))

        self.ui.radioButton_3.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[3],3))
        self.ui.radioButton_4.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[4],4))
        self.ui.radioButton_5.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[5],5))

        self.ui.radioButton_6.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[6],6))
        self.ui.radioButton_7.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[7],7))
        self.ui.radioButton_8.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[8],8))

        self.ui.radioButton_9.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[9],9))
        self.ui.radioButton_10.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[10],10))
        self.ui.radioButton_11.clicked.connect(partial(self.saveSelectOptions, \
         radioBttns[11],11))

        # Connect up the menu options
        self.ui.actionSelect_Profile.triggered.connect(lambda: \
                                                     self.openProfileLoader())
      
        # JAW - console code
        # hard coded text in console      
        self.ui.Console.append("Starting RosLaunch Console") 
        self.ui.Console.append("=======================") 
        self.ui.Console.append("ROS core INITIATED...........") 
        self.ui.Console.append("Simulator READY.............")
        # Remember to pass the definition/method, not the return value!

        self.loadPreviousOptions()
        

    #def loadConfiguration(self):
    #    #this is where the config will be read in and radio buttons remnamed


    def saveSelectOptions(self, name, rank):
        tmp="radioButton_"
        arch = file_archive('saveConfig.txt', serialized=True)
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

        #arch = configparser.ConfigParser()
        #arch.read('configData.ini')

        #try:
        #    arch = configparser.ConfigParser()
        #    with open("configData.ini", "r+") as f:
        #        arch.readfp(f)
        #except:
        #    arch = configparser.ConfigParser()
        #    #with open("configData.ini", "a") as f:
        #    #    arch.readfp(f)
        #if rank==1 or rank==4 or rank==7 or rank==10:
        #    if arch.has_section(name) == False:
        #        if arch.has_section(tmp+str(rank+1)):
        #            arch.remove_section(tmp+str(rank+1))
        #        if arch.has_section(tmp+str(rank-1)):
        #            print("\n\nhere\n\n")
        #            arch.remove_section(tmp+str(rank-1))
        #        arch.add_section(name)
        #        arch.set(name,'is_on','y')
        #        try:
        #            print("\n\nalso here\n\n")
        #            f.seek(0)
        #            arch.write(f)
        #            f.truncate()
        #            f.close()
        #        except:
        #            with open('configData.ini', 'a') as configfile:
        #                arch.write(configfile)
        #                    
        #elif rank==0 or rank==3 or rank==6 or rank==9:
        #    if arch.has_section(name) == False:
        #        if arch.has_section(tmp+str(rank+1)):
        #            arch.remove_section(tmp+str(rank+1))
        #        if arch.has_section(tmp+str(rank+2)):
        #            arch.remove_section(tmp+str(rank+2))
        #        arch.add_section(name)
        #        arch.set(name,'is_on','y')
        #        with open('configData.ini', 'a') as configfile:
        #            arch.write(configfile)
        #        configfile.close()
        #else: #rank==2 or rank==5 or rank==8 or rank==11
        #    if arch.has_section(name) == False:
        #        if arch.has_section(tmp+str(rank-1)):
        #            arch.remove_section(tmp+str(rank-1))
        #        if arch.has_section(tmp+str(rank-2)):
        #            arch.remove_section(tmp+str(rank-2))
        #        arch.add_section(name)
        #        arch.set(name,'is_on','y')
        #        with open('configData.ini', 'a') as configfile:
        #            arch.write(configfile)
        #        configfile.close()
           
    def loadPreviousOptions(self):
        arch = file_archive('saveConfig.txt')
        dictionary = arch.archive
        #print(dictionary)
        for i in dictionary:
            if 'y' == dictionary[i]:
                #print(i)
                var=getattr(self.ui, i)
                var.toggle()
            #dictionary[i] = 'n'

    def generateLaunchVars(self):
        params = []
        arch = file_archive('saveConfig.txt')
        dictionary = arch.archive
        print()
        print(dictionary)
        for i in dictionary:
            if 'y' == dictionary[i]:
                params.append(i)
                print(i)
                print(params)

        print(params)
        os.putenv('PARAMS', ' '.join(params))
        #param2 = params.pop(1)
       # param3 = params.pop(2)
       # param4 = params.pop(3)
        print(params)
        subprocess.call(['./runLaunch.sh >> kpw_logfile.txt'], shell=True)
        #print()
        #print(mapping)
        #print(percep)
        #print(rstrat)
        #print(planning)

        #for var in radioBttns:
        #    if radioBttn[var].isChecked():
        #        print(var)    
         
        #config = configparser.ConfigParser()
        #config.read('configData.ini')
        #for section in config.sections():
        #    for key in config[section]:
        #        if config[section][key] == 'y':
        #            var=getattr(self.ui, section)
        #            var.toggle()

        
    def startCarBttnAction(self):
        # This is executed when the button is pressed
        self.ui.Console.append("Starting Car....")
        self.generateLaunchVars()
        #subprocess.call(['./runSSH.sh >> kpw_logFile.txt'], shell=True)


    def startSimBttnAction(self):
        # This is executed when the button is pressed
        #print('Run Sim Button Pressed')
        self.ui.Console.append("Simulator RUNNING....")
        #os.system('./runSim.sh >> logfile_sim.txt &')
        global proc_sim
        proc_sim = subprocess.Popen(['screen -dmSL jaw ./runSim.sh &'], \
                                            shell=True,preexec_fn=os.setsid)
    def emergencyBttnAction(self):
        # This is executed when the button is pressed
        self.ui.Console.append("Stop the Car....")
       # subprocess.call(['./stopCar.sh >> kpw_logfile.txt'], shell=True)

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
        #returns string
        fname = dialog.getExistingDirectory(None, ("Select Folder")) 
        ROSWorkspacePath = "~" + fname
        self.profile_ui.ROSWSField.setText(fname) #element 0 is our file path
        # print(ROSWorkspacePath)
        self.model = QFileSystemModel()
        self.model.setRootPath(ROSWorkspacePath)
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index( \
                                                    QtCore.QDir.currentPath()))
        

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
        #subprocess.call(['./closeScreen.sh >> kpw_logFile.txt'], shell=True)
# End ImageDialog Class



if __name__ == "__main__":
    #proc_roscore=subprocess.Popen(['roscore &'], \
    #                        shell=True,preexec_fn=os.setsid)
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ImageDialog()
    #ui.setupUi(window)
    ui.show()
    #ui.openProfileLoader()
    sys.exit(app.exec_())
    



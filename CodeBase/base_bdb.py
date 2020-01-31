#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel
from profileSelect import Ui_ProfileSelect
from clientUI import Ui_MainWindow
import sys
import subprocess
import socket 
import os
import signal

# JAW - closure of ROS
import atexit
# JAW - saving config window session
from klepto.archives import *

#variables
hostname = socket.gethostname()    
localIPAddress = socket.gethostbyname(hostname)
robotIPAddress = ""
ROSWorkspacePath = ""
proc_sim=0
radioBttns = []
radioBttnsMan = ["radioButton_0", "radioButton_1", "radioButton_2",
 "radioButton_3", "radioButton_4", "radioButton_5", "radioButton_6",
  "radioButton_7", "radioButton_8", "radioButton_9", "radioButton_10", "radioBttns_11"]

class ImageDialog(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ImageDialog, self).__init__()
       
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Make local modifications.
       
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
        self.ui.Console.append("ROS core INITIATED...........") 
        self.ui.Console.append("Simulator READY.............")
        # Remember to pass the definition/method, not the return value!

        self.loadPreviousConfig()
        
  
    def list_files(self, startpath):
        self.treeView.clear()
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            #print('{}{}/'.format(indent, os.path.basename(root)))
            self.treeView.append('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                #print('{}{}'.format(subindent, f))
                self.treeView.append('{}{}'.format(subindent, f))

    def startCarBttnAction(self):
        # This is executed when the button is pressed
        self.Console.append("Starting Car....")
        subprocess.call(['./runCar.sh >> &'], shell=True)

    def startSimBttnAction(self):
        # This is executed when the button is pressed
        #print('Run Sim Button Pressed')
        self.ui.Console.append("Simulator RUNNING....")
        os.system('./runSim.sh >> logfile_sim.txt &')
        #print(proc_sim)
        #proc_sim = subprocess.Popen(['./runSim.sh >> logfile_sim.txt &',ROSWorkspacePath],shell=True,preexec_fn=os.setsid)

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

    @QtCore.pyqtSlot(QtCore.QModelIndex)                                                                                                                                                                            
    def populateEditor(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())

        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)

        self.ui.textBrowser.setText(fileName)
        #self.ui.textBrowser.setText(filePath)

        text = open(filePath, 'r').read()
        self.ui.textBrowser.setPlainText(text)

    #def getRadioBttns(self, array):
        #maybe latter
        
    #load previous config button options
    def loadPreviousConfig(self):
        try:
            with open("saveData.txt") as savedData:
                for line in savedData:
                   
                
                self.ui.Console.append("Previous options found")


        except FileNotFoundError:
            self.ui.Console.append("Previous options not found")

    # JAW - closure of ROS
    @atexit.register
    def closeROS():
        print("Begin killing program...")
        nodes = os.popen("rosnode list").readlines()
        for i in range(len(nodes)):
            nodes[i] = nodes[i].replace("\n","")
        for node in nodes:
            os.system("rosnode kill "+ node)
        #os.killpg(proc_sim.pid,signal.SIGTERM)
        os.killpg(proc_roscore.pid,signal.SIGTERM)
        

if __name__ == "__main__":
    proc_roscore=subprocess.Popen(['roscore &'],shell=True,preexec_fn=os.setsid)
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ImageDialog()
    #ui.setupUi(window)
    ui.show()
    #ui.openProfileLoader()
    sys.exit(app.exec_())
    



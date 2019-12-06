#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowTest1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from profileSelect import Ui_profileSelect
from PyQt5.QtWidgets import QFileDialog
import sys
import subprocess
import socket 
import os


#variables
hostname = socket.gethostname()    
localIPAddress = socket.gethostbyname(hostname)
robotIPAddress = ""
ROSWorkspacePath = ""

class Ui_MainWindow(object):
    
    def list_files(self, startpath):
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
        subprocess.call(['./autoSSH.sh'], shell=True)

    def startSimBttnAction(self):
        # This is executed when the button is pressed
        #print('Run Sim Button Pressed')
        self.Console.append("Simulator RUNNING....")
        subprocess.call(['./runSim.sh >> logfile_sim.txt &', ROSWorkspacePath], shell=True)

    def logContentsFromFile(self):
        curr_wkg_dir = os.getcwd()
        myfile = QtCore.QFile(curr_wkg_dir+"/logfile_sim.txt")
        myfile.open(QtCore.QIODevice.ReadOnly)
        stream = QtCore.QTextStream(myfile)
        content = stream.read(200)
        self.Console.append("Logging Contents from Simulation")
        self.Console.append("================================")
        # TODO: read one line at a time and translate
        myfile.close()
        self.Console.append(content)

    def createProfile(self):
        robotIPAddress = self.ui.robotIPLabel.text
        ROSWorkspacePath = self.ui.ROSWSField.text
        self.window.close()

    
    def openProfileLoader(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_profileSelect()
        self.ui.setupUi(self.window)
        self.ui.localIPAddressField.setText(localIPAddress)
        self.ui.browseROSWSBttn.clicked.connect(self.filePicker)
        self.ui.createProfileBttn.clicked.connect(self.createProfile)
        self.window.show()

    def filePicker(self):
        dialog = QFileDialog()
        #fname = dialog.getOpenFileName(None, "Window name", "", "Open Save Directory") #returns a tuple so need fname[0]
        fname = dialog.getExistingDirectory(None, ("Select Folder"))#returns string
        print(fname)
        self.ui.ROSWSField.setText(fname) #element 0 is our file path
        print(ROSWorkspacePath)
        self.list_files(str(fname))

    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 955)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.treeView = QtWidgets.QTextBrowser(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 0, 180, 431))
        self.treeView.setObjectName("treeView")

        self.StartCarBttn = QtWidgets.QPushButton(self.centralwidget)
        self.StartCarBttn.setGeometry(QtCore.QRect(1010, 790, 170, 48))
        self.StartCarBttn.setObjectName("StartCarBttn")
        self.StartCarBttn.clicked.connect(self.startCarBttnAction)
        
        self.runSimBttn = QtWidgets.QPushButton(self.centralwidget)
        self.runSimBttn.setGeometry(QtCore.QRect(1010, 720, 170, 48))
        self.runSimBttn.setObjectName("runSimBttn")
        self.Console = QtWidgets.QTextBrowser(self.centralwidget)
        # JAW - console code
        # hard coded text in console      
        self.Console.append("Starting RosLaunch Console") 
        self.Console.append("=======================") 
        ## print stuff from rosecore execution to Console
        #curr_wkg_dir = os.getcwd()
        #with open(curr_wkg_dir+"/logfile_core.txt") as fp:
        #    line = fp.readline()
        #    cnt = 1
        #    line = fp.readline()
        #    while line and (cnt < 4):
        #        if cnt != 2:
        #            self.Console.append("ROS core initiation: {}".format(line.strip()))
        #        line = fp.readline()
        #        cnt += 1
        ## hard coded text in console      
        self.Console.append("ROS core INITIATED...........") 
        self.Console.append("Simulator READY.............")
        # Remember to pass the definition/method, not the return value!
        self.runSimBttn.clicked.connect(self.startSimBttnAction) 
        self.runSimBttn.clicked.connect(self.logContentsFromFile)
        
        self.Console.setGeometry(QtCore.QRect(10, 720, 991, 192))
        self.Console.setObjectName("Console")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(190, 0, 991, 671))
        self.tabWidget.setObjectName("tabWidget")
        self.ConfigTab = QtWidgets.QWidget()
        self.ConfigTab.setObjectName("ConfigTab")
        self.scrollArea = QtWidgets.QScrollArea(self.ConfigTab)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 991, 641))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 989, 639))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.racingStrat = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.racingStrat.setGeometry(QtCore.QRect(0, 0, 981, 141))
        self.racingStrat.setObjectName("racingStrat")
        self.radioButton_9 = QtWidgets.QRadioButton(self.racingStrat)
        self.radioButton_9.setGeometry(QtCore.QRect(20, 50, 212, 40))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.racingStrat)
        self.radioButton_10.setGeometry(QtCore.QRect(270, 50, 212, 40))
        self.radioButton_10.setObjectName("radioButton_10")
        self.mappingBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.mappingBox.setGeometry(QtCore.QRect(370, 150, 230, 490))
        self.mappingBox.setAlignment(QtCore.Qt.AlignCenter)
        self.mappingBox.setObjectName("mappingBox")
        self.radioButton_11 = QtWidgets.QRadioButton(self.mappingBox)
        self.radioButton_11.setGeometry(QtCore.QRect(10, 50, 212, 40))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(self.mappingBox)
        self.radioButton_12.setGeometry(QtCore.QRect(10, 110, 212, 40))
        self.radioButton_12.setObjectName("radioButton_12")
        self.perceptionBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.perceptionBox.setGeometry(QtCore.QRect(0, 150, 230, 490))
        self.perceptionBox.setAlignment(QtCore.Qt.AlignCenter)
        self.perceptionBox.setObjectName("perceptionBox")
        self.radioButton_13 = QtWidgets.QRadioButton(self.perceptionBox)
        self.radioButton_13.setGeometry(QtCore.QRect(10, 50, 141, 40))
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(self.perceptionBox)
        self.radioButton_14.setGeometry(QtCore.QRect(10, 110, 121, 40))
        self.radioButton_14.setObjectName("radioButton_14")
        self.planningBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.planningBox.setGeometry(QtCore.QRect(750, 150, 230, 490))
        self.planningBox.setAlignment(QtCore.Qt.AlignCenter)
        self.planningBox.setObjectName("planningBox")
        self.radioButton_15 = QtWidgets.QRadioButton(self.planningBox)
        self.radioButton_15.setGeometry(QtCore.QRect(10, 110, 212, 40))
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_16 = QtWidgets.QRadioButton(self.planningBox)
        self.radioButton_16.setGeometry(QtCore.QRect(10, 50, 212, 40))
        self.radioButton_16.setObjectName("radioButton_16")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.ConfigTab, "")
        self.EditorTab = QtWidgets.QWidget()
        self.EditorTab.setObjectName("EditorTab")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.EditorTab)
        self.scrollArea_2.setGeometry(QtCore.QRect(-3, -3, 991, 651))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 989, 649))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 991, 641))
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.EditorTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 39))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionSelect_Profile = QtWidgets.QAction(MainWindow)
        self.actionSelect_Profile.setObjectName("actionSelect_Profile")
        self.menuFile.addAction(self.actionSelect_Profile)
        self.actionSelect_Profile.triggered.connect(lambda: self.openProfileLoader())
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RosLauncher"))
        self.StartCarBttn.setText(_translate("MainWindow", "Start Car"))
        self.runSimBttn.setText(_translate("MainWindow", "Run Sim"))
        self.racingStrat.setTitle(_translate("MainWindow", "Racing Strategy"))
        self.radioButton_9.setText(_translate("MainWindow", "option1"))
        self.radioButton_10.setText(_translate("MainWindow", "option 2"))
        self.mappingBox.setTitle(_translate("MainWindow", "Mapping"))
        self.radioButton_11.setText(_translate("MainWindow", "option1"))
        self.radioButton_12.setText(_translate("MainWindow", "option2"))
        self.perceptionBox.setTitle(_translate("MainWindow", "Perception"))
        self.radioButton_13.setText(_translate("MainWindow", "camera"))
        self.radioButton_14.setText(_translate("MainWindow", "lidar"))
        self.planningBox.setTitle(_translate("MainWindow", "Planning"))
        self.radioButton_15.setText(_translate("MainWindow", "option2"))
        self.radioButton_16.setText(_translate("MainWindow", "option1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ConfigTab), _translate("MainWindow", "Configuration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EditorTab), _translate("MainWindow", "Editor"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionSelect_Profile.setText(_translate("MainWindow", "Select Profile"))
        


if __name__ == "__main__":
    #subprocess.call(['roscore &'], shell=True)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.openProfileLoader()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowTest1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 0, 161, 351))
        self.treeView.setObjectName("treeView")
        
        self.StartCarBttn = QtWidgets.QPushButton(self.centralwidget)
        self.StartCarBttn.setGeometry(QtCore.QRect(630, 470, 170, 48))
        self.StartCarBttn.setObjectName("StartCarBttn")
        
        self.runSimBttn = QtWidgets.QPushButton(self.centralwidget)
        self.runSimBttn.setGeometry(QtCore.QRect(630, 410, 170, 48))
        self.runSimBttn.setObjectName("runSimBttn")
        self.runSimBttn.clicked.connect(self.startSimBttnAction)
        
        self.logBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.logBrowser.setGeometry(QtCore.QRect(10, 360, 611, 192))
        self.logBrowser.setObjectName("logBrowser")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSet_ROS_Workspace = QtWidgets.QAction(MainWindow)
        self.actionSet_ROS_Workspace.setObjectName("actionSet_ROS_Workspace")
        self.menuFile.addAction(self.actionSet_ROS_Workspace)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RosLauncher"))
        self.StartCarBttn.setText(_translate("MainWindow", "Start Car"))
        self.runSimBttn.setText(_translate("MainWindow", "Run Sim"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionSet_ROS_Workspace.setText(_translate("MainWindow", "Set ROS Workspace"))

    def startSimBttnAction(self):
        # This is executed when the button is pressed
        print('Run Sim Button Pressed')
        subprocess.call(['./runSim.sh'], shell=True)


if __name__ == "__main__":
    import sys

    subprocess.call(['roscore &'], shell=True)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

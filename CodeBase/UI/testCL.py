# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestCL.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 219)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.StartCarBttn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.StartCarBttn.sizePolicy().hasHeightForWidth())
        self.StartCarBttn.setSizePolicy(sizePolicy)
        self.StartCarBttn.setObjectName("StartCarBttn")
        self.gridLayout_2.addWidget(self.StartCarBttn, 0, 0, 1, 1)
        self.runSimBttn = QtWidgets.QPushButton(self.groupBox)
        self.runSimBttn.setObjectName("runSimBttn")
        self.gridLayout_2.addWidget(self.runSimBttn, 1, 0, 1, 1)
        self.stopCarBttn = QtWidgets.QPushButton(self.groupBox)
        self.stopCarBttn.setObjectName("stopCarBttn")
        self.gridLayout_2.addWidget(self.stopCarBttn, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 2, 1, 1)
        self.Console = QtWidgets.QTextEdit(self.centralwidget)
        self.Console.setObjectName("Console")
        self.gridLayout.addWidget(self.Console, 2, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Profile = QtWidgets.QAction(MainWindow)
        self.actionLoad_Profile.setObjectName("actionLoad_Profile")
        self.actionSave_Profile = QtWidgets.QAction(MainWindow)
        self.actionSave_Profile.setObjectName("actionSave_Profile")
        self.menuFile.addAction(self.actionLoad_Profile)
        self.menuFile.addAction(self.actionSave_Profile)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ROSConnect"))
        self.StartCarBttn.setText(_translate("MainWindow", "Start Car"))
        self.runSimBttn.setText(_translate("MainWindow", "Run Sim"))
        self.stopCarBttn.setText(_translate("MainWindow", "Stop Car"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Profile.setText(_translate("MainWindow", "Load Profile"))
        self.actionSave_Profile.setText(_translate("MainWindow", "Save Profile"))


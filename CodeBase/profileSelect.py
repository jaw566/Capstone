# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'ProfileSelect.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_profileSelect(object):
    
    def setupUi(self, profileSelect):
        profileSelect.setObjectName("profileSelect")
        self.gridLayout = QtWidgets.QGridLayout(profileSelect)
        self.gridLayout.setObjectName("gridLayout")
        self.localIPLabel = QtWidgets.QLabel(profileSelect)
        self.localIPLabel.setObjectName("localIPLabel")
        self.gridLayout.addWidget(self.localIPLabel, 0, 0, 1, 1)
        self.localIPAddressField = QtWidgets.QLineEdit(profileSelect)
        self.localIPAddressField.setObjectName("localIPAddressField")
        self.gridLayout.addWidget(self.localIPAddressField, 0, 1, 1, 2)
        self.robotIPLabel = QtWidgets.QLabel(profileSelect)
        self.robotIPLabel.setObjectName("robotIPLabel")
        self.gridLayout.addWidget(self.robotIPLabel, 1, 0, 1, 1)
        self.ROSWSField = QtWidgets.QLineEdit(profileSelect)
        self.ROSWSField.setObjectName("ROSWSField")
        self.gridLayout.addWidget(self.ROSWSField, 2, 1, 1, 2)
        self.robotIPField = QtWidgets.QLineEdit(profileSelect)
        self.robotIPField.setObjectName("robotIPField")
        self.gridLayout.addWidget(self.robotIPField, 1, 1, 1, 2)
        self.rosWSLabel = QtWidgets.QLabel(profileSelect)
        self.rosWSLabel.setObjectName("rosWSLabel")
        self.gridLayout.addWidget(self.rosWSLabel, 2, 0, 1, 1)
        self.openProfileBttn = QtWidgets.QPushButton(profileSelect)
        self.openProfileBttn.setObjectName("openProfileBttn")
        self.gridLayout.addWidget(self.openProfileBttn, 5, 1, 1, 1)
        self.createProfileBttn = QtWidgets.QPushButton(profileSelect)
        self.createProfileBttn.setObjectName("createProfileBttn")
        self.gridLayout.addWidget(self.createProfileBttn, 5, 2, 1, 1)
        self.browseROSWSBttn = QtWidgets.QPushButton(profileSelect)
        self.browseROSWSBttn.setObjectName("browseROSWSBttn")
        self.gridLayout.addWidget(self.browseROSWSBttn, 3, 2, 1, 1)

        self.retranslateUi(profileSelect)
        QtCore.QMetaObject.connectSlotsByName(profileSelect)

    def retranslateUi(self, profileSelect):
        _translate = QtCore.QCoreApplication.translate
        profileSelect.setWindowTitle(_translate("profileSelect", "Profile Select"))
        self.localIPLabel.setText(_translate("profileSelect", "Local IP Address"))
        self.robotIPLabel.setText(_translate("profileSelect", "Robots IP Address"))
        self.rosWSLabel.setText(_translate("profileSelect", "ROS Workspace"))
        self.openProfileBttn.setText(_translate("profileSelect", "Open"))
        self.createProfileBttn.setText(_translate("profileSelect", "Create"))
        self.browseROSWSBttn.setText(_translate("profileSelect", "Browse"))


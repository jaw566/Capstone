# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProfileSelect2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProfileSelect(object):
    def setupUi(self, ProfileSelect):
        ProfileSelect.setObjectName("ProfileSelect")
        ProfileSelect.resize(484, 232)
        self.centralwidget = QtWidgets.QWidget(ProfileSelect)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        self.browseROSWSBttn = QtWidgets.QPushButton(self.centralwidget)
        self.browseROSWSBttn.setObjectName("browseROSWSBttn")
        self.gridLayout.addWidget(self.browseROSWSBttn, 3, 3, 1, 1)
        self.openProfileBttn = QtWidgets.QPushButton(self.centralwidget)
        self.openProfileBttn.setObjectName("openProfileBttn")
        self.gridLayout.addWidget(self.openProfileBttn, 4, 2, 1, 1)
        self.createProfileBttn = QtWidgets.QPushButton(self.centralwidget)
        self.createProfileBttn.setObjectName("createProfileBttn")
        self.gridLayout.addWidget(self.createProfileBttn, 4, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.localIPLabel = QtWidgets.QLabel(self.centralwidget)
        self.localIPLabel.setMaximumSize(QtCore.QSize(120, 16777215))
        self.localIPLabel.setObjectName("localIPLabel")
        self.gridLayout.addWidget(self.localIPLabel, 0, 0, 1, 1)
        self.robotIPLabel = QtWidgets.QLabel(self.centralwidget)
        self.robotIPLabel.setMaximumSize(QtCore.QSize(120, 16777215))
        self.robotIPLabel.setObjectName("robotIPLabel")
        self.gridLayout.addWidget(self.robotIPLabel, 1, 0, 1, 1)
        self.rosWSLabel = QtWidgets.QLabel(self.centralwidget)
        self.rosWSLabel.setMaximumSize(QtCore.QSize(120, 16777215))
        self.rosWSLabel.setObjectName("rosWSLabel")
        self.gridLayout.addWidget(self.rosWSLabel, 2, 0, 1, 1)
        self.ROSWSField = QtWidgets.QLineEdit(self.centralwidget)
        self.ROSWSField.setObjectName("ROSWSField")
        self.gridLayout.addWidget(self.ROSWSField, 2, 1, 1, 3)
        self.robotIPField = QtWidgets.QLineEdit(self.centralwidget)
        self.robotIPField.setObjectName("robotIPField")
        self.gridLayout.addWidget(self.robotIPField, 1, 1, 1, 3)
        self.localIPAddressField = QtWidgets.QLineEdit(self.centralwidget)
        self.localIPAddressField.setObjectName("localIPAddressField")
        self.gridLayout.addWidget(self.localIPAddressField, 0, 1, 1, 3)
        ProfileSelect.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfileSelect)
        QtCore.QMetaObject.connectSlotsByName(ProfileSelect)

    def retranslateUi(self, ProfileSelect):
        _translate = QtCore.QCoreApplication.translate
        ProfileSelect.setWindowTitle(_translate("ProfileSelect", "Profile Select"))
        self.browseROSWSBttn.setText(_translate("ProfileSelect", "Browse"))
        self.openProfileBttn.setText(_translate("ProfileSelect", "Open"))
        self.createProfileBttn.setText(_translate("ProfileSelect", "Create"))
        self.localIPLabel.setText(_translate("ProfileSelect", "Local IP Address"))
        self.robotIPLabel.setText(_translate("ProfileSelect", "Robot IP Address"))
        self.rosWSLabel.setText(_translate("ProfileSelect", "ROS Workspace"))


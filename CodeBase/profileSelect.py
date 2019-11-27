# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProfileSelect.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profileSelect(object):
    def setupUi(self, profileSelect):
        profileSelect.setObjectName("profileSelect")
        profileSelect.resize(600, 300)
        self.openProfileBttn = QtWidgets.QPushButton(profileSelect)
        self.openProfileBttn.setGeometry(QtCore.QRect(370, 260, 100, 35))
        self.openProfileBttn.setObjectName("openProfileBttn")
        self.createProfileBttn = QtWidgets.QPushButton(profileSelect)
        self.createProfileBttn.setGeometry(QtCore.QRect(480, 260, 100, 35))
        self.createProfileBttn.setObjectName("createProfileBttn")
        self.localIPLabel = QtWidgets.QLabel(profileSelect)
        self.localIPLabel.setGeometry(QtCore.QRect(10, 20, 240, 35))
        self.localIPLabel.setObjectName("localIPLabel")
        self.robotIPLabel = QtWidgets.QLabel(profileSelect)
        self.robotIPLabel.setGeometry(QtCore.QRect(10, 80, 240, 35))
        self.robotIPLabel.setObjectName("robotIPLabel")
        self.rosWSLabel = QtWidgets.QLabel(profileSelect)
        self.rosWSLabel.setGeometry(QtCore.QRect(10, 140, 240, 35))
        self.rosWSLabel.setObjectName("rosWSLabel")
        self.localIPAddressField = QtWidgets.QLineEdit(profileSelect)
        self.localIPAddressField.setGeometry(QtCore.QRect(270, 20, 240, 35))
        self.localIPAddressField.setObjectName("localIPAddressField")
        self.robotIPField = QtWidgets.QLineEdit(profileSelect)
        self.robotIPField.setGeometry(QtCore.QRect(270, 80, 240, 35))
        self.robotIPField.setObjectName("robotIPField")
        self.ROSWSField = QtWidgets.QLineEdit(profileSelect)
        self.ROSWSField.setGeometry(QtCore.QRect(270, 140, 240, 35))
        self.ROSWSField.setObjectName("ROSWSField")
        self.browseROSWSBttn = QtWidgets.QPushButton(profileSelect)
        self.browseROSWSBttn.setGeometry(QtCore.QRect(390, 190, 120, 35))
        self.browseROSWSBttn.setObjectName("browseROSWSBttn")

        self.retranslateUi(profileSelect)
        QtCore.QMetaObject.connectSlotsByName(profileSelect)

    def retranslateUi(self, profileSelect):
        _translate = QtCore.QCoreApplication.translate
        profileSelect.setWindowTitle(_translate("profileSelect", "Profile Select"))
        self.openProfileBttn.setText(_translate("profileSelect", "Open"))
        self.createProfileBttn.setText(_translate("profileSelect", "Create"))
        self.localIPLabel.setText(_translate("profileSelect", "Local IP Address"))
        self.robotIPLabel.setText(_translate("profileSelect", "Robots IP Address"))
        self.rosWSLabel.setText(_translate("profileSelect", "ROS Workspace"))
        self.browseROSWSBttn.setText(_translate("profileSelect", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profileSelect = QtWidgets.QWidget()
    ui = Ui_profileSelect()
    ui.setupUi(profileSelect)
    profileSelect.show()
    sys.exit(app.exec_())

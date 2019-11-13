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
        profileSelect.resize(400, 300)
        self.openProfileBttn = QtWidgets.QPushButton(profileSelect)
        self.openProfileBttn.setGeometry(QtCore.QRect(200, 260, 89, 25))
        self.openProfileBttn.setObjectName("openProfileBttn")
        self.createProfileBttn = QtWidgets.QPushButton(profileSelect)
        self.createProfileBttn.setGeometry(QtCore.QRect(300, 260, 89, 25))
        self.createProfileBttn.setObjectName("createProfileBttn")
        self.localIPLabel = QtWidgets.QLabel(profileSelect)
        self.localIPLabel.setGeometry(QtCore.QRect(20, 30, 111, 17))
        self.localIPLabel.setObjectName("localIPLabel")
        self.robotIPLabel = QtWidgets.QLabel(profileSelect)
        self.robotIPLabel.setGeometry(QtCore.QRect(20, 70, 131, 17))
        self.robotIPLabel.setObjectName("robotIPLabel")
        self.rosWSLabel = QtWidgets.QLabel(profileSelect)
        self.rosWSLabel.setGeometry(QtCore.QRect(20, 110, 111, 17))
        self.rosWSLabel.setObjectName("rosWSLabel")
        self.localIPAddressField = QtWidgets.QLineEdit(profileSelect)
        self.localIPAddressField.setGeometry(QtCore.QRect(160, 30, 171, 25))
        self.localIPAddressField.setObjectName("localIPAddressField")
        self.robotIPField = QtWidgets.QLineEdit(profileSelect)
        self.robotIPField.setGeometry(QtCore.QRect(160, 70, 171, 25))
        self.robotIPField.setObjectName("robotIPField")
        self.ROSWSField = QtWidgets.QLineEdit(profileSelect)
        self.ROSWSField.setGeometry(QtCore.QRect(160, 110, 171, 25))
        self.ROSWSField.setObjectName("ROSWSField")
        self.browseROSWSBttn = QtWidgets.QPushButton(profileSelect)
        self.browseROSWSBttn.setGeometry(QtCore.QRect(268, 140, 61, 25))
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

# as Im not sure that the textBrowser in base.py is the browser botton I 
# just made a sample display for fileBrowser and Im not sure it works or 
# not

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.fileBrowser = QtWidgets.QPushButtom(self)
        self.fileBrowser.setObjectName("fileBrowser")
        self.fileBrowser.setText("Test")
        self.fileBrowser.clicked.connect(self.msg)

    def msg(self):
        directory1 = QFileDialog.getExistingDirectory(self, "select folder", "./")
        print(directory1)

        fileName1, filetype = QFileDialog.getOpenFileName(self, "select file", "./", "All Files (*);;Text File (*.txt)")
        # Set file extension filtering, separated by double semicolons

        print(fileName1, filetype)

        files, ok1 = QFileDialog.getOpenFileNames(self, "multiply files selection", "./" "All Files (*);;Text Files (*.txt)")
        print(files,ok1)

        fileName2, ok2 = QFileDialog.getSaveFileName(self, "file saved", "./", "All Files (*);;Text File (*.txt)")

if __name__=="__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show() 
    sys.exit(app.exec_())      

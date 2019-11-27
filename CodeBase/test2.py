#This test has ROS runing and the Simulation
#All hard coded

from PyQt5 import QtWidgets, uic
import sys
import subprocess

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('MainWindowTest1.ui', self) # Load the .ui file


        #get the run sim button
        self.startSimBttn = self.findChild(QtWidgets.QPushButton, 'runSimBttn')
        self.startSimBttn.clicked.connect(self.startSimBttnAction) # Remember to pass the definition/method, not the return value!


        self.show() # Show the GUI
    
    def startSimBttnAction(self):
        # This is executed when the button is pressed
        print('Run Sim Button Pressed')
        subprocess.call(['./runSim.sh'], shell=True)
        
subprocess.call(['roscore &'], shell=True)
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
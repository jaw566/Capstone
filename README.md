# Capstone
CS capstone repository for project: Autonomous F1/10 Racing for Everyone

## Getting Started for Development

First we need to make sure pip3 is installed

`sudo apt install python3-pip`

PyQt5 is the core of our software so we need to install that

`pip3 install pyqt5`

We will also need Sphinx

`sudo apt-get install python3-sphinx`

## Take it for a Spin
If everything worked you should be able to run the base.py file 

`python3 ./base.py`

*Note this has to be done in the CodeBase Directory*

## Using the PyQt Designer
If you want to use the designer you navigate to the pyqt bin

`cd /usr/lib/x86_64-linux-gnu/qt5/bin/`

Then we can run the designer

`./designer`

After you have saved your UI file you cna run the following command to generate a python file with all the objets generated.

`pyuic5 -x UI_FILE_NAME.ui -o NAME_OF_EXC.py`

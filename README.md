# Capstone
CS capstone repository for project: Autonomous F1/10 Racing for Everyone

## Getting Started for Development

First we need to make sure pip3 is installed

`sudo apt install python3-pip`

Now we get Pipenv, a python enviorment control tool

`sudo pip3 install pipenv`

Move to the CodeBase folder where you cloned the repository 

`cd ~/Capstone/CodeBase/`

Finally run the setup command

`pipenv install`

We will also need Sphinx

`sudo apt-get install python3-sphinx`

## Take it for a Spin
If everything worked you should be able to start the python env with 

`pipenv shell`

*Note this has to be done in the CodeBase Directory*

Now we can launch the test.py file

`python3 test.py`

*If the test.py file can not find PyQt5 your pipenv is either not running or not set up correctly*

## Using the PyQt Designer
If you want to use the designer you navigate to the pyqt bin

`cd /usr/lib/x86_64-linux-gnu/qt5/bin/`

Then we can run the designer

`./designer`

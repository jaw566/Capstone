#!/bin/bash

echo $1 | sudo -S apt-get install python3-pip

echo " "

echo $1 | sudo -S apt-get install screen=4.6.2-1ubuntu1

echo " "

echo $1 | sudo -S apt-get install python3-sphinx

echo 

echo $1 | sudo -S apt-get install python3-pyqt5

echo " "

echo $1 | sudo -S apt-get install sshpass

echo " "

pip3 install pyyaml

echo " "

pip3 install klepto==0.1.8


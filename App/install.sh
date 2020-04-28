#!/bin/bash

password= $1

echo $password |sudo -S apt install python3-pip=9.0.1

echo $password |sudo -S apt-get install screen=4.06.02 

echo $password |sudo -S apt-get install python3-sphinx=1.8.5

pip3 install pyqt5

pip3 install pyyaml==5.3

pip3 install klepto==0.1.8

#!/bin/bash

# Description: this script is used to set up the RosConnect system by installing all necessary dependencies,
#              changing the password for running the vehicles via 'ssh', and creating a desktop icon for starting
#              the RosConnect application

cd ~/RosConnect/App

./install.sh $1 # raspberry Pi password

./mk_all_password_instances.py $2 # vehicle password

/bin/cp RosConnect.desktop $HOME/Desktop

./init_desktop_file.py

/bin/cp run_gui.sh $HOME 

/bin/cp logo.png $HOME






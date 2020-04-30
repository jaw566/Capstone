#!/bin/bash

# Description: this script is used to set up the RosConnect system by installing all necessary dependencies,
#              changing the password for running the vehicles via 'ssh', and creating a desktop icon for starting
#              the RosConnect application

cd ~/RosConnect/App

./install.sh $1 # raspberry Pi password

./mk_hostname_and_password.py $2 $3 $4 # vehicle host_id hostname and password (in that order)

/bin/cp RosConnect.desktop $HOME/Desktop

./init_desktop_file.py

/bin/cp run_gui.sh $HOME 

/bin/cp logo.png $HOME






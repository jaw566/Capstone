#!/bin/bash

# Description: this script is used to set up the RosConnect system by installing all necessary dependencies,
#              changing the password for running the vehicles via 'ssh', and creating a desktop icon for starting
#              the RosConnect application

if [ "$#" -ne 4 ]; then
    echo "You must run setup with exactly 4 command line arguments as follows:"
    echo "./setup.sh [host_password] [vehicle_ip] [vehicle_hostname] [vehicle_password]"
    exit
fi

cd ~/RosConnect/App

./install.sh $1 # raspberry Pi password

./mk_hostname_and_password.py $2 $3 $4 # vehicle ip hostname and password (in that order)

/bin/cp RosConnect.desktop $HOME/Desktop

./init_desktop_file.py

/bin/cp run_gui.sh $HOME 

/bin/cp logo.png $HOME






#!/bin/bash

cd ~/Capstone/CodeBase/App
./mk_all_password_instances.py password_here
/bin/cp RosConnect.desktop $HOME/Desktop
./init_desktop_file.py
/bin/cp run_gui.sh $HOME 
/bin/cp logo.png $HOME






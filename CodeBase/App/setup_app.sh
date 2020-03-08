#!/bin/bash

# /usr/bin/test -f ${XDG_CONFIG_HOME:-~/.config}/user-dirs.dirs && source ${XDG_CONFIG_HOME:-~/.config}/user-dirs.dirs

cd ~/Capstone/CodeBase/App
#/bin/cp RosConnect.desktop ${XDG_DESKTOP_DIR:-$HOME/Desktop} 
/bin/cp RosConnect.desktop $HOME/Desktop
./init_desktop_file.py
/bin/cp run_gui.sh $HOME 
/bin/cp logo.png $HOME






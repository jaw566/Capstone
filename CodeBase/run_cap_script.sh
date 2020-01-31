#!/bin/bash

scp cap_script.sh nvidia@10.18.92.118:~/Documents

#ssh nvidia@10.18.92.118 'cd ~/Documents; screen -S jaw; ./cap_script.sh >> jaw_logfile.txt' 
ssh nvidia@10.18.92.118 'cd ~/Documents; nohup ./cap_script.sh >> jaw_logfile.txt' 


#!/bin/bash 

sshpass -p 'Doan1234' scp sshTest.sh runClose.sh runStop.sh nvidia@10.18.92.118:'~/Documents'

sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'screen -dmS roscore; pwd'  #creates the screen

sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'screen -dmS ssh; pwd'  #creates the screen

sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'cd ~/Documents; screen -r ssh; ./sshTest.sh >> kpw_logfile.txt'  #replace with a launch file 


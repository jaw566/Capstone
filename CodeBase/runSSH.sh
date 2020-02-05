#!/bin/bash 

sshpass -p 'Doan1234' scp sshTest.sh nvidia@10.18.92.118:'~/Documents'


sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 screen -D -R -S ssh 'cd ~/Documents; ./sshTest.sh >> logfile.txt'  #replace sshTest.sh with the launch file

sshpass -p 'Doan1234' ssh -T nivdia@10.18.92.118 screen -d #detaches the screen 

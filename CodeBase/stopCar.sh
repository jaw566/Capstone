#!/bin/bash
sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'cd ~/Documents; screen -r; ./runStop.sh >> kpw_logfile.txt'  #replace with a launch file  

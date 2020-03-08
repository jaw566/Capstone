#!/bin/bash

sshpass -p 'doan_1234' ssh -T nvidia@10.18.92.160 'cd ~/Documents; screen -r; rm kpw_logfile.txt runStop.sh sshTest.sh runSim.sh runLaunch.sh'

sshpass -p 'doan_1234' ssh -T nvidia@10.18.92.160 'cd ~/Documents; screen -r; ./runClose.sh'


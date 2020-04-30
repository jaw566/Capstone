#!/bin/bash

sshpass -p 'password' ssh -T nvidia@10.18.92.120 'cd ~/Documents; screen -r; rm runStop.sh runSim.sh runLaunch.sh carStop.sh'

sshpass -p 'password' ssh -T nvidia@10.18.92.120 'cd ~/Documents; screen -r; ./runClose.sh'



#!/bin/bash

sshpass -p 'newpassword' ssh -T nvidia@10.18.92.160 'cd ~/Documents; screen -r; rm runStop.sh runSim.sh runLaunch.sh carStop.sh'

sshpass -p 'newpassword' ssh -T nvidia@10.18.92.160 'cd ~/Documents; screen -r; ./runClose.sh'



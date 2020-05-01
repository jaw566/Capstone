#!/bin/bash

sshpass -p 'test' ssh -T test@10.18.92.130 'cd ~/Documents; screen -r; rm runStop.sh runSim.sh runLaunch.sh carStop.sh'

sshpass -p 'test' ssh -T test@10.18.92.130 'cd ~/Documents; screen -r; ./runClose.sh'



#!/bin/bash

sshpass -p 'password' ssh -T 10.19.18.160@nvidia 'cd ~/Documents; screen -r; rm runStop.sh runSim.sh runLaunch.sh carStop.sh'

sshpass -p 'password' ssh -T 10.19.18.160@nvidia 'cd ~/Documents; screen -r; ./runClose.sh'



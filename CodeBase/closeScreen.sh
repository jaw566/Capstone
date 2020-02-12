#!/bin/bash

sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'cd ~/Documents; screen -r; rm kpw_logfile.txt runStop.sh sshTest.sh'

sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'cd ~/Documents; screen -r; ./runClose.sh'


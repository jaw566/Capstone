#!/bin/bash 

sshpass -p 'Doan1234' scp sshTest.sh nvidia@10.18.92.118:'~/Documents'


sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'cd ~/Documents; nohup ./sshTest.sh >> logfile.txt'


#!/bin/bash 
echo $@ 


#Pass Files over to car
sshpass -p 'password' scp runClose.sh runLaunch.sh runSim.sh carStop.sh 10.19.18.160@nvidia:'~/Documents'

#Create the ssh screen - to enteract and close files with
sshpass -p 'password' ssh -T 10.19.18.160@nvidia 'screen -dmS Ssh'

#This reconnects roscore screen and passes the launch file to it to execute.  
# sshpass -p 'doan_1234' ssh -T nvidia@10.18.92.160 "cd ~/Documents; screen -r 
#roscore; ./runLaunch.sh ${@}>> kpw_logfile.txt"  #replace with a launch file
sshpass -p 'password' ssh -T 10.19.18.160@nvidia "screen -dmS roscore ./runCar.sh"

echo "Successfully running car"


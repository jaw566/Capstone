#!/bin/bash 
echo $@ 


#Pass Files over to car
sshpass -p 'newpassword' scp runClose.sh runStop.sh runLaunch.sh runSim.sh carStop.sh nvidia@10.18.92.160:'~/Documents'

#Create the ssh screen - to enteract and close files with
sshpass -p 'newpassword' ssh -T nvidia@10.18.92.160 'screen -dmS Ssh'

#This reconnects roscore screen and passes the launch file to it to execute.  
# sshpass -p 'doan_1234' ssh -T nvidia@10.18.92.160 "cd ~/Documents; screen -r roscore; ./runLaunch.sh ${@}>> kpw_logfile.txt"  #replace with a launch file
sshpass -p 'newpassword' ssh -T nvidia@10.18.92.160 "screen -dmS roscore ./runCar.sh"

echo "Successfully running car"


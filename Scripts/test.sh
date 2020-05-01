#!/bin/bash 
echo $@ 

echo " "
#Pass Files over to car
echo sshpass -p 'test' scp runClose.sh runStop.sh runLaunch.sh runSim.sh carStop.sh test@10.18.92.130:'~/Documents'

#Create the ssh screen - to enteract and close files with
echo sshpass -p 'test' ssh -T test@10.18.92.130 'screen -dmS Ssh'
echo " " 
#This reconnects roscore screen and passes the launch file to it to execute.  
# sshpass -p 'doan_1234' ssh -T nvidia@10.18.92.160 "cd ~/Documents; screen -r 
#roscore; ./runLaunch.sh ${@}>> kpw_logfile.txt"  #replace with a launch file
echo sshpass -p 'test' ssh -T test@10.18.92.130 "screen -dmS roscore ./runCar.sh"
echo " "
echo "Successfully running car"


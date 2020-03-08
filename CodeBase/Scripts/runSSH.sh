#!/bin/bash 
echo $@ 


#Pass Files over to car
sshpass -p 'doan_1234' scp sshTest.sh runClose.sh runStop.sh runLaunch.sh runSim.sh nvidia@10.18.92.160:'~/Documents'

#Create the roscore screen. This is where we will run the program.
sshpass -p 'doan_1234' ssh -T nvidia@10.18.92.160 'screen -dmS roscore' 

#Create the ssh screen. This is what we will enteract with and close files with. 
sshpass -p 'doan_1234' ssh -T nvidia@10.18.92.160 'screen -dmS Ssh'  

sshpass -p 'doan_1234' ssh -T nvidia@10.18.92.160 'cd ~/Documents; screen -r Ssh; ./sshTest.sh >> kpw_logfile.txt'  #replace with a launch file 

#This reconnects roscore screen and passes the launch file to it to execute.  
sshpass -p 'doan_1234' ssh -T nvidia@10.18.92.160 "cd ~/Documents; screen -r roscore; ./runLaunch.sh ${@}>> kpw_logfile.txt"  #replace with a launch file


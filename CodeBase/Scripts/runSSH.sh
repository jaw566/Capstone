#!/bin/bash 

#Pass Files over to car
sshpass -p 'Doan1234' scp sshTest.sh runClose.sh runStop.sh nvidia@10.18.92.118:'~/Documents'

#Create the roscore screen. This is where we will run the program.
sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'screen -dmS roscore; pwd' 

#Create the ssh screen. This is what we will enteract with and close files with. 
sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'screen -dmS ssh; pwd'  

sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'cd ~/Documents; screen -r ssh; ./sshTest.sh >> kpw_logfile.txt'  #replace with a launch file 

#This reconnects roscore screen and passes the launch file to it to execute.  
sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'cd ~/Documents; screen -r roscore; ./runLaunch.sh >> kpw_logfile.txt'  #replace with a launch file


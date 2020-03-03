#!/bin/bash 

echo $@ >> kpw_log.txt

ssh kyle@localhost 'cd ~/Documents/Capstone/CodeBase/Scripts; ./runLaunch.sh "$1"' >> kpw_log.txt

#Pass Files over to car
echo sshpass -p 'Doan1234' scp sshTest.sh runClose.sh runStop.sh nvidia@10.18.92.118:'~/Documents' >>kpw_logfile.txt

#Create the roscore screen. This is where we will run the program.
echo sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'screen -dmS roscore; pwd'>>kpw_logfile.txt 

#Create the ssh screen. This is what we will enteract with and close files with. 
echo sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'screen -dmS ssh; pwd'  >>kpw_logfile.txt

echo sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'cd ~/Documents; screen -r ssh; ./sshTest.sh >> kpw_logfile.txt'>>kpw_logfile.txt  #replace with a launch file 

#This reconnects roscore screen and passes the launch file to it to execute.  
echo sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'cd ~/Documents; screen -r roscore; ./runLaunch.sh >> kpw_logfile.txt' >>kpw_logfile.txt  #replace with a launch file


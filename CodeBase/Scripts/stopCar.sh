#!/bin/bash
sshpass -p 'Doan1234' ssh -T nvidia@10.18.92.118 'cd ~/Documents; screen -r ssh; ./runStop.sh >> kpw_logfile.txt'  #replace with a launch file  

PROC_NAME=$1  
ProcNumber=`ps -ef |grep -w $PROC_NAME|grep -v grep|wc -l`  
if [ $ProcNumber -le 0 ];then  
   result=0  
else  
   result=1   
fi  
echo ${result}

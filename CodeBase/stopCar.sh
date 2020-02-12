#!/bin/bash  
PROC_NAME=$1  
ProcNumber=`ps -ef |grep -w $PROC_NAME|grep -v grep|wc -l`  
if [ $ProcNumber -le 0 ];then  
   result=0  
else  
   result=1   
fi  
echo ${result}

#!/usr/bin/env python3
import subprocess
import os, sys, string
import re
def closeROS():
    print("Start killing program...")
    os.system('export ROS_HOSTNAME=localhost')
    os.system('export ROS_MASTER_URI=http://localhost:11311')
    nodes = os.popen("rosnode list").readlines()
    for i in range(len(nodes)):
        nodes[i] = nodes[i].replace("\n","")
    for node in nodes:
        os.system("rosnode kill "+ node)
    if( 'proc_sim' in globals()):
        os.system("screen -S jaw -X quit")
    if( 'proc_roscore' in globals()):
        os.killpg(proc_roscore.pid,signal.SIGTERM)
x = 1
if __name__ == "__main__":
    closeROS()

if(x == 1):
    print(' ros processes been closed successfully, the car stopped')
else:
    print(' false to stop the car')

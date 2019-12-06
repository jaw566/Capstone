#!/bin/bash
USERNAME=nvidia
HOSTS="10.18.92.233"
SCRIPT="password; yes"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done
cd ~/f110_ws
source devel/setup.bash
roslaunch racecar teleop.launch && fg
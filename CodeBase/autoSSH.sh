#!/bin/bash
USERNAME=nvidia
HOSTS="10.18.92.233"
SCRIPT="password; yes
cd ~/f110_ws
source devel/setup.bash
roslaunch racecar teleop.launch && fg"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done

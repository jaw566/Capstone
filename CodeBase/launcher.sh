#!/bin/bash

# _Desc
# The purpose of this script is to run the ROSLAUNCH application remotely.
# Preconditions: non-local machine must contain directory ".ssh";
#                local machine must have private/public key generated and
#                the following two steps are pressumed complete on local machine
#                in order to bypass passphrase prompt:
#                1. ssh-keygen -t rsa
#                2. cat ~/.ssh/id_rsa.pub | ssh user@hostname 'cat >>
#                   .ssh/authorized_keys'.
#
# _Auth
# Jordan Wright
#
# _Date
# 01-26-2020
#
# _Vers
# Version 1.0



ssh user@hostname 'cd $ROSLAUNCHER; nohup ./base_bdb.py' &




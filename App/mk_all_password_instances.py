#!/usr/bin/env python3

# Description: Loop through all files in Scripts directory and set the password (to be used in ssh call)
#              to the password argument given by the caller of this function

import os
import sys

def main():

    if len(sys.argv) != 2:
        print("Incorrect number of arguments given")
        print("Please use as ./fix_all_password_instances [password]")
        return -1
    
    password = str(sys.argv[1])

    HOME  = os.environ['HOME']

    files = os.listdir(HOME+'/RosConnect/Scripts') 

    for f in files:
        with open(HOME+'/RosConnect/Scripts/'+f,'r') as file:
            data = file.readlines()

        line_ctr=0
        for line in data:
            line_split = line.split()
            if line_split != [] and line_split[0] == 'sshpass':
                line_split[2] = "'"+password+"'"
                data[ line_ctr ] = " ".join( line_split )+"\n"
            line_ctr+=1

        with open(HOME+'/RosConnect/Scripts/'+f,'w') as file:
            file.writelines(data)

if __name__ == "__main__":

    main()    


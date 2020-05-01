#!/usr/bin/env python3

# Description: Loop through all files in Scripts directory and set the password (to be used in ssh call)
#              to the password argument given by the caller of this function

import os
import sys

def main():

    if len(sys.argv) != 4:
        print("Incorrect number of arguments given")
        print("Please run as ./mk_hostname_and_password [vehicle_id]  [vehicle_hostname] [password]")
        print("e.g., ./mk_hostname_andpassword 10.18.92.120 nvidia password")
        return -1
    
    host = str(sys.argv[1])
    hostname = str(sys.argv[2])
    password = str(sys.argv[3])

    HOME  = os.environ['HOME']

    files = os.listdir(HOME+'/RosConnect/Scripts') 

    for f in files:
        with open(HOME+'/RosConnect/Scripts/'+f,'r') as file:
            data = file.readlines()

        line_ctr=0
        for line in data:
            line_split = line.split()
            if line_split != [] and line_split[0] == 'sshpass':
                host_ctrl =0
                ctrl = 0
                for param in line_split:
                   if "@" in param:
                       host_values = param.split("@")
                       host_values[0] = host
                       host_name = host_values[0]
                       host_ip = host_values[1]
                       if ":" in host_ip:
                           host_value = host_ip.split(":")
                           host_value[0] = hostname
                           second = host_value[1]
                           new_host = host_value[0] + ":"+second 
                       else:
                           host_values[1] = hostname
                           new_host = host_values[1]
                       new_param = host_name + "@"+new_host
                       param = new_param
                       line_split[host_ctrl] = param
                   host_ctrl+= 1 
                line_split[2] = "'"+password+"'"
                data[ line_ctr ] = " ".join( line_split )+"\n"
            line_ctr+=1

        with open(HOME+'/RosConnect/Scripts/'+f,'w') as file:
             file.writelines(data)

if __name__ == "__main__":
    main()

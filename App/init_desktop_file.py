#!/usr/bin/env python3

import os

def main():

    HOME = os.environ['HOME']
    
    with open(HOME+'/Desktop/RosConnect.desktop','r') as file:
        data = file.readlines()

    data[4] = "Icon="+HOME+"/logo.png\n"

    with open(HOME+'/Desktop/RosConnect.desktop','w') as file:
        file.writelines(data)

if __name__ == "__main__":

    main()    


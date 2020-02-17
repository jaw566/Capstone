#!/usr/bin/env python3
import subprocess
import os, sys, string
import re

result = 1
if __name__ == '__main__':
    p = subprocess.getoutput("pgrap roscore")
    subprocess.getoutput("kill %s" %p)
    result = 0

if(result == 0):
    print("The roscore been closed, the car stop successfully")
else: 
    print("Roscore failed to close")

#!/bin/bash
rm runClose.sh	

pkill ros

screen -XS Ssh quit
screen -XS roscore quit

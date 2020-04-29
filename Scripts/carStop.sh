#!/bin/bash


sshpass -p 'password' ssh -T nvidia@10.18.92.160 "pkill ros"

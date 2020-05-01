#!/bin/bash

echo ""
echo "Stopping Car"
echo "------------"
echo sshpass -p 'password' ssh -T 10.19.18.160@nvidia "pkill ros"
echo "------------"
echo ""

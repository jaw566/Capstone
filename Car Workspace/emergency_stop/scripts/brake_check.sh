#!/bin/bash
function checkScreen()
{
    if ! screen -list | grep -q "Ssh";
    then
        return 1
    else
        return 0
    fi
}

checkScreen
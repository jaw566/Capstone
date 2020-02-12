#!/bin/bash

#echo Last passed parameter is ${!#}

if [ -n "$1" ]; then

    arg1 = $1

    for var in ${arg1[@]}
    do
	    echo "arrray: $var"
    done 
    echo Racing Strategy: $1
    echo Percetpion:      $2
    echo Mapping:         $3
    echo Planning:        $4

else

    echo "No parameters found. "

fi

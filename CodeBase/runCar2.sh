cd ~/f110_ws                             #This will change to the directory where code is stored. 
#pwd
source devel/setup.bash                  #Source the package to run. 
roslaunch racecar teleop.launch && fg    #Run so the car can work with the remote. 

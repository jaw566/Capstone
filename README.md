# RosConnect
RosConnect is a graphical user interface that allows you to drive an F1/10 vehicle autonomously. This improvement of access to autonomous racing means that the Yellowtails project can provide a learning platform to people with limited coding experience.

Through our new cutting edge graphical user interface, new coders will be able to utilize the F1/10 platform to start autonomous racing. By abstracting the Robotic Operating System (ROS) and the comand line interface we lower the entry level of autonomuos racing.

Learn more at our [website](https://www.cefns.nau.edu/capstone/projects/CS/2020/Yellowtails-S20/index.html).

<details><summary><strong>Installation Instructions</strong></summary>
<p>
These instructions will get you a copy of the project up and running on your local machine.

### Installing

A step by step series of examples that tell you how to get the software running.

For this software to work ROS must be insalled on the host machine. To learn how to install ROS visit [ROS.org](https://www.ros.org/)

Clone the repo into the home directroy

```
cd ~/ && git clone https://github.com/jaw566/RosConnect.git
```

Run the setup script

```
cd ~/RosConnect/App/ && ./setup.sh [host_password] [vehicle_password] [host_name]
```

### Simulator Setup

In order to run the simulators you need to install and source the simulator.

We need the ros-kinetic-map-server to run the simutor

```
sudo apt-get install ros-kinetic-map-server
```

Make a new workspace for the simulator

```
mkdir -p ~/f110_ros/src
cd ~/f110_ros/src
catkin_init_workspace
```
 
Clone the simulator
 
```
cd ~/f110_ros/src && git clone https://github.com/FF1RR-NAU-Spring-2020/ff1rr-2020-spring.git
``` 
 
Make the workspace with catkin_make and source the ﬁle

```
cd ~/f110_ros/
catkin_make
source devel/setup.bash
```

To make the simulator work with out sourcing it every time add the source command to your bashrc file
 
```
echo 'source ~/ff110_ros/devel/setup.bash' >> ~/.bashrc
```

## Take it for a Spin
If everything worked you should be able to run RosConnect.

There is now be a desktop icon/file called RosConnect.

Double click the file and then select 'Trust and Launch' to start the software.

You can also run the software via the commandline

```
cd ~/RosConnect/ && ./main.py
```

</p>
</details>

<details><summary><strong>PyQt Development</strong></summary>
<p>

## Using the PyQt Designer
If you want to use the designer you navigate to the pyqt bin

`cd /usr/lib/x86_64-linux-gnu/qt5/bin/`

Then we can run the designer

`./designer`

After you have saved your UI file you cna run the following command to generate a python file with all the objets generated.

`pyuic5 -x UI_FILE_NAME.ui -o NAME_OF_EXC.py`
</p>
</details>

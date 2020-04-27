# Capstone
The Yellowtails project is a graphical user interface that allows you to drive an F1/10 vehicle autonomously. This improvement of access to autonomous racing means that the Yellowtails project can provide a learning platform to people with limited coding experience.

Through our new cutting edge graphical user interface, new coders will be able to utilize the F1/10 platform to start autonomous racing. By abstracting the Robotic Operating System (ROS) and the comand line interface we lower the entry level of autonomuos racing.

Learn more at our [website](https://www.cefns.nau.edu/capstone/projects/CS/2020/Yellowtails-S20/index.html).

<details><summary><strong>Installation Instructions</strong></summary>
<p>
These instructions will get you a copy of the project up and running on your local machine.

### Installing

A step by step series of examples that tell you how to get the software running
For this software to work ROS must be insalled on the host machine. To learn how to install ROS visit [ROS.org](https://www.ros.org/)

Clone the repo into the home directroy

```
cd ~/ git clone https://github.com/jaw566/Capstone.git
```

Run the setup script

```
cd ~/Capstone/Codebase/App/ ./setup.sh
```
There is now a desktop icon/file called RosConnect. Double clcke the file and then selct Trust and Launch to start the software.


###Sourcing


End with an example of getting some data out of the system or using it for a little demo
</p>
</details>

<details><summary><strong>Getting Started for Development</strong></summary>
<p>
First we need to make sure pip3 is installed

`sudo apt install python3-pip`

PyQt5 is the core of our software so we need to install that

`pip3 install pyqt5`

For our configuration system we need PyYaml to parse our .yaml files

`pip3 install pyyaml`

For saving user selections on exit and relaoding then on launch we are using Klepto

`pip3 install klepto`

We will also need Screen

`sudo apt-get install screen`

We will also need Sphinx

`sudo apt-get install python3-sphinx`

## Take it for a Spin
If everything worked you should be able to run the base.py file 

`python3 ./base.py`

*Note this has to be done in the CodeBase Directory*

## Using the PyQt Designer
If you want to use the designer you navigate to the pyqt bin

`cd /usr/lib/x86_64-linux-gnu/qt5/bin/`

Then we can run the designer

`./designer`

After you have saved your UI file you cna run the following command to generate a python file with all the objets generated.

`pyuic5 -x UI_FILE_NAME.ui -o NAME_OF_EXC.py`
</p>
</details>

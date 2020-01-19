# RaspberryAQ-Controller

This is a little side project of mine, wich helps me to learn programming and work with diffrent tecnologys.
Then currently im not a sofware engineer. 


## Getting Started

This controller is based on the programming language python and does currently just use one libary that has to be installed.
But no worries i got an easy installscript ready for you.
Its setup to control a mainlight based on time, a CO2 solanoid based on time and controll your heater with the help of a DS18B20
temprature sensor.

### Hardware
#### RaspberryPi
The controller software is tested on the following hardware:
* Raspberry Pi 4B 4GB

The controller software is going to be testet on the following hardware:
* Raspberry Pi 3B

#### Relays
Disclaimer: If you don't have any expirience working with mains voltage, you must get help from a professional!

I use a Relayboard with 4 relays wich can be directly connectet to the RaspberryPi
By default the following pins are setup to switch the relays:
```python
heater_relay = 36
mainlight_relay = 38
co2_relay = 40
```

#### Temprature sensor
The RaspberryAQ-Controller supports just the DS18B20 temprature sensor.
They are inexpensive and come in a waterproof form.
And the installation script handels the configuration for you.

Verkabelungs shema einfügen !

### Installing
To install the RasperryAQ-Controller we recomend to download the newest Raspian with the Desktop image and installing it on your Pi.
When you install the Rapian without the dektop, you can't use our GUI. 
[Official Source](https://www.raspberrypi.org/downloads/raspbian/)

First update your PI.
This can take a few minutes, it depends on your internet speed and your connection type.
```bash
sudo apt update
sudo apt upgrade -y
```

Then install git, to get the RaspberryAQ-Controller software.
```bash
sudo apt install git
```

After you installd git, its time to download the software.
```bash
cd ~
git clone https://github.com/puchtuning/RaspberryAQ-Controller.git
```

Now you can install the software with our install script.
This script will automatically reboot your system, after its done installing.
```bash
cd RaspberryAQ-Controller/_install/
sudo bash install.sh
```
**Make sure to run this script just once! Otherwise it corrupts your files.**
We are working on a solution for that.


## Running the RaspberryAQ-Controller
Before yout can run any test, its important to connect yout temprature sensor.
Otherwise the cotroller just spits out errors.

### Running the GUI
If you have installed a Raspbian version with desktop you can proceed with this step.
If not you can read the topic **Configure per commandline** to learn how to setup your RaspberryAQ-Controller.

First open the commandline and copy and paste the following commands.
The second command starts the GUI.
```bash
cd ~/RraspberryAQ-Controller/
python3 GUI-AQ-controller.py
```
In the GUI you can choose on wich times and temperatures your controller should perform wich task.
The timeformat is in european time: 08:00 AM = 20:00
When all values right set, you car save the configfile an close the GUI Window.

The GUI is currently under construction and will be updated over time.

### Configure per commandline
To configure your controller via commandline, you need to opber de inputfile with the following command.
```bash
sudo nano ~/RaspberryAQ-Controller/data/_controller-input.json
```
Then you will be greeted, with a file in wich you can edit your values as you like.

```json
{
    "Controller-input": {
        "timestamp": "18.01.2020 23:36:18",
        "aq_main_light_on": "20:00",
        "aq_main_light_off": "20:00",
        "aq_co2_on": "20:00",
        "aq_co2_off": "20:00",
        "aq_temp": "28"
    }
}
```
**The timeformat is in european time: 08:00 AM = 20:00**
After you changed the values, you can save the file and close it.

### Starting the Server

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - Coding environment
* [Python 3.8.1](https://www.python.org/) - Programming language
* [MySQL Python Connector](https://dev.mysql.com/doc/connector-python/en/) - Python libary

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Pascal alias puchtuning** - *Initial work* - [puchtuning](https://github.com/puchtuning)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The Ben Hack Show
* [ReefSpy with the ReefberryPi](https://www.youtube.com/channel/UCvuGXFKFf4DIs2AD7Gjc_Kw)



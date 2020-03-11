# RaspberryAQ-Controller

This is a little side project of mine, wich helps me to learn programming and work with different technologies. Then currently im not a software engineer.

## Getting Started

This controller is based on the programming language python (V3.6+) and does currently just use one libary that has to be installed.
But no worries i got an easy installscript ready for you.
Its setup to control a mainlight based on time, a CO2 solanoid based on time and your heater with the help of a DS18B20 temprature sensor.

### Hardware

#### RaspberryPi

The controller software was tested on the following hardware:

* Raspberry Pi 4B 4GB
* Raspberry Pi 3B

The controller software is going to be testet on the following hardware:

* Currently no test are running

#### Relays

**Disclaimer: If you don't have any experience working with mains voltage, you must get help from a professional!**

I use a relayboard with 4 relays, wich can be directly connectet to the RaspberryPi.
By default the following pins are setup to switch the relays:

```python
heater_relay = 36
mainlight_relay = 38
co2_relay = 40
```

#### Temprature sensor

The RaspberryAQ-Controller supports just the DS18B20 temprature sensor. They are inexpensive and come in a waterproof form.
And the installation script handels the configuration for you.

![alt text](https://i.stack.imgur.com/5EKzW.png)

### Installing the RaspberryAQ-Controller

To install the RasperryAQ-Controller we recomend to download the newest Raspian with the Desktop image and installing it on your Pi.
When you install the Raspian without the dektop, you can't use our GUI.
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

Now you can install the software with our install script. The script will check what is installed and install the missing components.
This script will automatically reboot your system, after its done installing.

```bash
sudo bash /RaspberryAQ-Controller/_install/install.sh
```

## Running the RaspberryAQ-Controller

Before yout can run any test, its important to connect yout temprature sensor.
Otherwise the cotroller just spits out errors.

### Configure per GUI

If you have installed a Raspbian version with desktop you can proceed with this step.

If not you can read the topic **Configure per commandline** to learn how to setup your RaspberryAQ-Controller.

First open the commandline and copy and paste the following commands.
The second command starts the GUI.

```bash
cd ~/RaspberryAQ-Controller/_GUI/
python3 GUI-AQ-controller.py
```

In the GUI you can choose on wich times and temperatures your controller should perform wich task.
The timeformat is in european time: 08:00 PM = 20:00

When all values right set, you can save the configfile an close the GUI Window.

### Configure per commandline

To configure your controller via commandline, you need to open the inputfile with the following command.

```bash
sudo nano ~/RaspberryAQ-Controller/data/_controller-input.json
```

Then you will be greeted, with a file in wich you can edit your values as you like.

```json
{
    "Controller-input": {
        "timestamp": "25.01.2020 15:50:52",
        "aq_main_light_on": "10:00",
        "aq_main_light_off": "21:00",
        "aq_co2_on": "11:00",
        "aq_co2_off": "21:00",
        "aq_temp": "24",
        "MYSQL": {
            "useMYSQL": false,
            "HOST": "MYSQL_HOST",
            "DBNAME": "MYSQL_DATABASE",
            "USERNAME": "MYSQL_USER",
            "PASSWD": "MYSQL_PASSWD",
            "CONTROLLERID": "Controller_ID"
        }
    }
}
```

**The timeformat is in european time: 08:00 PM = 20:00**
After you changed the values, you can save the file and close it.

### MYSQL Connector

If you want to write the controller data to a mysql database, you can configure it thru the GUI or the command line. This should be self explanatory.

Create a database with a table called "aq_controller", with the following rows:

* ID (auto auto_increment)
* Controller_ID (TEXT)
* aq_timestamp (TEXT)
* aq_temp (TEXT)
* aq_heater (TEXT)
* aq_mainlight (TEXT)
* aq_co2_dosing (TEXT)

### Starting the Server

First open the commandline and copy and paste the following commands.
The second command starts the Server, wich controls the all the things.

```bash
python3 ~/RraspberryAQ-Controller/Server-AQ-controller.py
```

The Server creats a useful terminal output to show you whats going on.
Additionally the server creates logfiles and datafiles wich can be used to display the informations on a webpage.
The data files get used by the GUI to display the informations.

## Deployment

To ensure that your RaspberryAQ-Controller is always starting with your Pi you need to add the Server into the crontab.

```bash
crontab -e
```

Add the following line to the bottom of the file and save it.

```bash
@reboot sleep 60 && cd RraspberryAQ-Controller/ && python3 Server-AQ-controller.py
```

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - Coding environment
* [Python 3.8.1](https://www.python.org/) - Programming language
* [MySQL Python Connector](https://dev.mysql.com/doc/connector-python/en/) - Python libary

## Authors

* **Pascal** - *Initial work* - [puchtuning](https://github.com/puchtuning)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The Ben Hack Show
* [ReefSpy with the ReefberryPi](https://www.youtube.com/channel/UCvuGXFKFf4DIs2AD7Gjc_Kw)
* [Andreas Spiess](https://www.youtube.com/channel/UCu7_D0o48KbfhpEohoP7YSQ)

## Disclaimer

The creators of the RaspberryAQ controller software take no liability for any damage or injury. When dealing with mains voltages, we advise you to contact a specialist.

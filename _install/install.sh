#!/bin/bash


echo "Setup 1-Wire bus for Temprature"
modprobe w1-gpio
modprobe w1-therm

echo "" >> /boot/config.txt
echo "#enables ds1850 temp reads" >> /boot/config.txt
echo "dtoverlay=w1-gpio" >> /boot/config.txt
#echo "dtoverlay=w1-gpio,gpioin=4,pullup=on" >> /boot/config.txt

echo "" >> /etc/modules
echo "w1_gpio" >> /etc/modules
echo "w1_therm" >> /etc/modules

echo "Installing libarys"

pip3 install -r requirements.txt


echo "Press any key to reboot:"

reboot
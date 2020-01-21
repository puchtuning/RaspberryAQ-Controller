#!/bin/bash

LOCCONF='/boot/config.txt'
LOCMODULES='/etc/modules'


CONFIGVAL1='dtoverlay=w1-gpio'
CONFIGVAL2='w1_gpio'
CONFIGVAL3='w1_therm'


CHECKFILE=$(grep 'dtoverlay=w1-gpio' $LOCCONF)

echo "Setup 1-Wire bus for Temprature"
modprobe w1-gpio
modprobe w1-therm


if [ "$CHECKFILE" == "$CONFIGVAL1" ]
then
    echo "config.txt is already setup"
else
    echo "" >> $LOCCONF
    echo "#enables ds1850 temp reads" >> $LOCCONF
    echo "dtoverlay=w1-gpio" >> $LOCCONF
    echo "config.txt is setup"
fi

CHECKFILE=$(grep 'w1_gpio' $LOCMODULES)

if [ "$CHECKFILE" == "$CONFIGVAL2" ]
then
    echo "mudules is already setup"
else
    echo "" >> $LOCMODULES
    echo "w1_gpio" >> $LOCMODULES
    echo "w1_therm" >> $LOCMODULES
    echo "mudules setup is written "
fi


echo "Installing libarys"

pip3 install -r requirements.txt

read -p "Press enter to reboot"

shutdown -r now
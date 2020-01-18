import time
import os
import xml.etree.cElementTree as ET
import xml.dom.minidom as dom
import mysql.connector #-Enables connection to MYSQL Database
import logging #-Enables to write Logfiles
import json #-To write/read the data Files


# ---Write-Frequency
# Default value is 5 Seconds
sleeptime = 5

# -----Controller-Values
Controller_ID = "Raps02test"

# -----mysql-connection infos
useMYSQL = "FALSE"
mydb = mysql.connector.connect(
    host="192.168.0.103",
    user="aq_controller",
    passwd="6010Kriens$",
    database="Aquarium"
)




# ---Functions Start

# ---Controller Input XML Function

def load_controller_input(xmlnode):
    print("Read controller input file")

    xmlinput = dom.parse("data\\_controller-input.xml")

    for eintrag in xmlinput.firstChild.childNodes:
        if eintrag.nodeName == "controller-input":
            for knoten in eintrag.childNodes:
                if(knoten.nodeName == xmlnode):
                    print(xmlnode + ": " + knoten.firstChild.data.strip())
                    xmlvalue = knoten.firstChild.data.strip()

    return(str(xmlvalue))

# --Initialize Logging
logtime = time.strftime("%Y-%m-%d")
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename="log\\" + logtime + "_RaspberryAQ.log", level=logging.INFO)

# --Initialize JSON
data_RaspberryAQ = {}

# --Functions Ende


aq_main_light_on = load_controller_input("aq_main_light_on")
aq_main_light_off = load_controller_input("aq_main_light_off")
aq_co2_on = load_controller_input("aq_co2_on")
aq_co2_off = load_controller_input("aq_co2_off")
aq_temp = load_controller_input("aq_temp")



logging.info('Server-RaspberryAQ Started!')

while True:

    # ---Get Times
    daytime = time.strftime("%H:%M")
    date = time.strftime("%d.%m.%Y")
    fulltime = time.strftime("%d.%m.%Y %H:%M:%S")

# ---Light Switching

    if(daytime >= aq_main_light_on and daytime <= aq_main_light_off):
        aq_main_light_status = "On"
        logging.info('Mainlight is switched on')
    else:
        aq_main_light_status = "Off"
        logging.info('Mainlight is switched off')

# ---CO2 Switching

    if(daytime >= aq_co2_on and daytime <= aq_co2_off):
        aq_co2_status = "On"
        logging.info('CO2 is switched on')

    else:
        aq_co2_status = "Off"
        logging.info('CO2 is switched off')


# ---Output
# --Terminal output
    print("---Controller Values---")
    print("--Date and Time--")
    print( "Date and Daytime: ",date, daytime)
    print("Fulltime: ",fulltime)
    print("--Light--")
    print("Target time light on", aq_main_light_on,
          "and licht off", aq_main_light_off)
    print("Light status: ", aq_main_light_status)

    print("--CO2--")
    print("Target time CO2 on", aq_co2_on, "and CO2 off", aq_co2_off)
    print("CO2 status: ", aq_co2_status)

    print("--Temprature--")
    print("Target temprature:", aq_temp)

# --SQL output

    if(useMYSQL == "TRUE"):
        mycursor = mydb.cursor()

        sql = "INSERT INTO aq_controller (Controller_ID, aq_timestamp, aq_mainlight, aq_temp, aq_heater) VALUES (%s, %s, %s, %s, %s)"
        val = (Controller_ID,  fulltime, aq_main_light_status, "0", "Off")
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    
# --Data File Output
    data_RaspberryAQ[fulltime] = {"aq_mainlight_status": aq_main_light_status, "aq_co2_status": aq_co2_status}

    with open("data\\"+ logtime + "_data_RaspberryAQ.json", 'w') as f:
        json.dump(data_RaspberryAQ, f)


# ---Delay
    time.sleep(sleeptime)

# ---Beauty-Command
    os.system('clear')  # Disabele for Debug

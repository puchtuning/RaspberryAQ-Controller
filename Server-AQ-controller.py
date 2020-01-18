import time
from datetime import datetime
import os
import mysql.connector  # -Enables connection to MYSQL Database
import logging  # -Enables to write Logfiles
import json  # -To write/read the data Files


# ---Write-Frequency
# Default value is 5 Seconds
sleeptime = 5

# -----Controller-Values
Controller_ID = "Raps02test"

# -----mysql-connection infos
useMYSQL = "FALSE"
host = "MYSQLHOSTNAME"
user = "USERNAME"
passwd = "PASSWORT"
database = "DBNAME"


# ----Get conntroller Input
checkinputfile = 60  # default is all 60 / all 5 minutes


# ---Functions Start
# ---Loop counters
loopcounterinput = checkinputfile

# ---Controller Input JSON Function


def load_controller_input(JSONnode):
    print("Read controller input file")

    inputJSON = open('data\\_controller-input.json')
    controllerinput = json.load(inputJSON)
    JSONnode = controllerinput['Controller-input'][JSONnode]

    return(str(JSONnode))


# --Initialize Logging
logtime = time.strftime("%Y-%m-%d")
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    filename="log\\" + logtime + "_Server-RaspberryAQ.log", level=logging.INFO)
logging.info('Server-RaspberryAQ Started!')

# --Initialize JSON
data_RaspberryAQ = {}
Controller_RaspberryAQ = {}

# --Functions Ende


aq_main_light_on = load_controller_input("aq_main_light_on")
aq_main_light_off = load_controller_input("aq_main_light_off")
aq_co2_on = load_controller_input("aq_co2_on")
aq_co2_off = load_controller_input("aq_co2_off")
aq_temp = load_controller_input("aq_temp")

# Reads the time at wich the inputfile was saved
lastinputtime = load_controller_input("timestamp")


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

# ---Check for new input file
    if(loopcounterinput >= checkinputfile):
        print("Check for new Input file")
        logging.info('Checking for new Input file.')
        inputtime = load_controller_input("timestamp")

        if(datetime.strptime(inputtime, "%d.%m.%Y %H:%M:%S") > datetime.strptime(lastinputtime, "%d.%m.%Y %H:%M:%S")):
            aq_main_light_on = load_controller_input("aq_main_light_on")
            aq_main_light_off = load_controller_input("aq_main_light_off")
            aq_co2_on = load_controller_input("aq_co2_on")
            aq_co2_off = load_controller_input("aq_co2_off")
            aq_temp = load_controller_input("aq_temp")
            lastinputtime = load_controller_input("timestamp")

            logging.info('Inputfile updated!')

        loopcounterinput = 0


# ---Output
# --Terminal output
    print("---Controller Values---")
    print("--Date and Time--")
    print("Date and Daytime: ", date, daytime)
    print("Fulltime: ", fulltime)
    print("--Light--")
    print("Target time light on", aq_main_light_on,"and licht off", aq_main_light_off)
    print("Light status: ", aq_main_light_status)

    print("--CO2--")
    print("Target time CO2 on", aq_co2_on, "and CO2 off", aq_co2_off)
    print("CO2 status: ", aq_co2_status)

    print("--Temprature--")
    print("Target temprature:", aq_temp)

# --SQL output

    if(useMYSQL == "TRUE"):
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO aq_controller (Controller_ID, aq_timestamp, aq_mainlight, aq_temp, aq_heater) VALUES (%s, %s, %s, %s, %s)"
        val = (Controller_ID,  fulltime, aq_main_light_status, "0", "Off")
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

# --Data File Output
    data_RaspberryAQ[fulltime] = {
        "aq_mainlight_status": aq_main_light_status, "aq_co2_status": aq_co2_status}

    with open("data\\" + logtime + "_data_RaspberryAQ.json", 'w') as f:
        json.dump(data_RaspberryAQ, f)

# ---Loop counters
    loopcounterinput = loopcounterinput + 1

# ---Delay
    time.sleep(sleeptime)

# ---Beauty-Command
    os.system('clear')  # Disabele for Debug

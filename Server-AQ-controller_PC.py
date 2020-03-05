
import os
import glob
import time
import datetime
from datetime import datetime

import logging  # -Enables to write Logfiles
import json  # -To write/read the data Files


test = 0

# ----Pinsetup (use BOARD pinaout)
extra_relay = 32
heater_relay = 36
mainlight_relay = 38
co2_relay = 40

# -----mysql-connection infos
writetomysql = 180  # default is 180 / all 15 minutes


# ---Write-Frequency
# Default value is 5 Seconds
sleeptime = 5

# ----Get conntroller Input
checkinputfile = 5  # default is 60 / all 5 minutes


# ---Functions Start
# ---Loop counters
loopcounterinput = checkinputfile
loopcountermysql = writetomysql
loopcounterdelete = 0
loopcountertest = 0

# -----GPIO-Configuration


# ---Text colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ---Controller Input JSON Function


def load_controller_input(JSONnode):
    # print("Read controller input file")

    inputJSON = open('data/_controller-input.json')
    controllerinput = json.load(inputJSON)
    JSONnode = controllerinput['Controller-input'][JSONnode]

    return(str(JSONnode))


def load_controller_mysql(JSONnode):
    # print("Read controller input file")

    inputJSON = open('data/_controller-input.json')
    controllerinput = json.load(inputJSON)
    JSONnode = controllerinput['Controller-input']['MYSQL'][JSONnode]

    return(str(JSONnode))

# --Write JSON
def writeDataFile(datatime, fulltime, aq_main_light_status, aq_co2_status, aq_heater_status, aq_temp_sen):

    with open("data/" + datatime + "_data_RaspberryAQ.json", 'w') as f:

        data_RaspberryAQ = {}

        data_RaspberryAQ['data'] = [
            {
            "timestamp": fulltime,
            "aq_mainlight_status": aq_main_light_status,
            "aq_co2_status": aq_co2_status,
            "aq_heater_status": aq_heater_status,
            "aq_temp_sen": aq_temp_sen
            }

        ]

        json.dump(data_RaspberryAQ, f, indent=4, sort_keys=True)




# --Initialize Logging
logtime = time.strftime("%Y-%m-%d")
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    filename="log/" + logtime + "_Server-RaspberryAQ.log", level=logging.INFO)
logging.info('Server-RaspberryAQ Started!')
print(f"{bcolors.OKGREEN}Server-RaspberryAQ Started!{bcolors.ENDC}")
time.sleep(5)

# --Temp-Function
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

"""
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                return temp_c

"""
# For debug without temp sensor


def read_temp():
    temp_c = 25.00
    return temp_c


# --Initialize JSON structure
data_RaspberryAQ = {}
# Controller_RaspberryAQ = {}

# --Functions Ende


# --Read Input File
try:
    aq_main_light_on = load_controller_input("aq_main_light_on")
    aq_main_light_off = load_controller_input("aq_main_light_off")
    aq_co2_on = load_controller_input("aq_co2_on")
    aq_co2_off = load_controller_input("aq_co2_off")
    aq_temp = load_controller_input("aq_temp")
    # Reads the time at wich the inputfile was saved
    lastinputtime = load_controller_input("timestamp")

    logging.info('Inputfile imported')

    aq_temp = float(aq_temp)

# --Reads the MYSQL Information
    useMYSQL = load_controller_mysql("useMYSQL")
    if(useMYSQL == 'True'):
        host = load_controller_mysql("HOST")
        user = load_controller_mysql("USERNAME")
        passwd = load_controller_mysql("PASSWD")
        database = load_controller_mysql("DBNAME")
        Controller_ID = load_controller_mysql("CONTROLLERID")
        logging.info('MYSQL Infos imported')
        print(f"{bcolors.OKGREEN}MYSQL Infos imported{bcolors.ENDC}")


except:
    print(f"{bcolors.WARNING}Warning: Inputfile couldn't be found!{bcolors.ENDC}")
    print(f"{bcolors.WARNING}Shuting down RasperryAQ-Server!{bcolors.ENDC}")
    logging.warning("Data: Inputfile couldn't be found!")
    exit()


while True:

    # ---Get Times
    daytime = time.strftime("%H:%M")
    date = time.strftime("%d.%m.%Y")
    datatime = time.strftime("%Y-%m-%d")
    fulltime = time.strftime("%d.%m.%Y %H:%M:%S")
    today = datetime.today()


# ---Light switching

    if(daytime >= aq_main_light_on and daytime <= aq_main_light_off):

        aq_main_light_status = "On"
        logging.info('Mainlight is switched on')
    else:

        aq_main_light_status = "Off"
        logging.info('Mainlight is switched off')

# ---CO2 switching

    if(daytime >= aq_co2_on and daytime <= aq_co2_off):

        aq_co2_status = "On"
        logging.info('CO2 is switched on')

    else:

        aq_co2_status = "Off"
        logging.info('CO2 is switched off')

# ---Temp switching

    aq_temp_sen = read_temp()

    if(aq_temp_sen <= aq_temp):

        aq_heater_status = "On"
        logging.info('Heater is switched on')
    else:

        aq_heater_status = "Off"
        logging.info('Heater is switched off')


# ---Output
# --Terminal output
    print(f"{bcolors.HEADER}---Controller Values---{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}--Date and Time--{bcolors.ENDC}")
    print("Date and Daytime: ", date, daytime)
    print("Fulltime: ", fulltime)
    print(f"{bcolors.OKBLUE}--Light--{bcolors.ENDC}")
    print("Target time light on", aq_main_light_on,
          "and licht off", aq_main_light_off)
    print("Light status: ", aq_main_light_status)

    print(f"{bcolors.OKBLUE}--CO2--{bcolors.ENDC}")
    print("Target time CO2 on", aq_co2_on, "and CO2 off", aq_co2_off)
    print("CO2 status: ", aq_co2_status)

    print(f"{bcolors.OKBLUE}--Temprature--{bcolors.ENDC}")
    print("Target temprature:", aq_temp_sen)
    print("Heater status: ", aq_heater_status)

    print(f"{bcolors.OKBLUE}--Other information--{bcolors.ENDC}")


# --Data File Output
    # try to Update JSON
    try:
        dataJSON = open("data/" + datatime + "_data_RaspberryAQ.json")
        controllerinput = json.load(dataJSON)
        JSONnode = controllerinput['data']


        #print(JSONnode)
        with open("data/" + datatime + "_data_RaspberryAQ.json", 'w') as f:



            data_RaspberryAQ = {


                "timestamp": fulltime,
                "aq_mainlight_status": aq_main_light_status,
                "aq_co2_status": aq_co2_status,
                "aq_heater_status": aq_heater_status,
                "aq_temp_sen": aq_temp_sen


            }
            #z = json.load(JSONnode)
            JSONnode.append(data_RaspberryAQ)

            json.dump(controllerinput, f, indent=4, sort_keys=True)


    # create JSON file
    except Exception:
        writeDataFile(datatime, fulltime, aq_main_light_status, aq_co2_status, aq_heater_status, aq_temp_sen)


# ---Check for new input file
    if(loopcounterinput >= checkinputfile):
        print("Check for new Input file")
        logging.info('Checking for new Input file.')
        try:
            inputtime = load_controller_input("timestamp")
        except:
            print(
                f"{bcolors.WARNING}Warning: Inputfile couldn't be found!{bcolors.ENDC}")
            print(f"{bcolors.WARNING}Running with old config.{bcolors.ENDC}")
            logging.warning("Data: Inputfile couldn't be found!")

        if(datetime.strptime(inputtime, "%d.%m.%Y %H:%M:%S") > datetime.strptime(lastinputtime, "%d.%m.%Y %H:%M:%S")):
            aq_main_light_on = load_controller_input("aq_main_light_on")
            aq_main_light_off = load_controller_input("aq_main_light_off")
            aq_co2_on = load_controller_input("aq_co2_on")
            aq_co2_off = load_controller_input("aq_co2_off")
            aq_temp = load_controller_input("aq_temp")
            aq_temp = float(aq_temp)
            lastinputtime = load_controller_input("timestamp")

            useMYSQL = load_controller_mysql("useMYSQL")
            if(useMYSQL == 'True'):
                host = load_controller_mysql("HOST")
                user = load_controller_mysql("USERNAME")
                passwd = load_controller_mysql("PASSWD")
                database = load_controller_mysql("DBNAME")
                Controller_ID = load_controller_mysql("CONTROLLERID")
                logging.info('MYSQL Infos imported')
                print(f"{bcolors.OKGREEN}MYSQL Infos imported{bcolors.ENDC}")

            print(f"{bcolors.OKGREEN}Inputfile updated!{bcolors.ENDC}")
            logging.info('Inputfile updated!')

        loopcounterinput = 0

# ---Delete old files
    if(daytime >= "23:19" and daytime <= "23:59"):
        print("These Files are Older than 7 Days")

        for i in glob.glob('/data/*'):
            print(i)
            t = os.stat(i)[8]
            filetime = datetime.datetime.fromtimestamp(t) - today
            print(filetime)
            if(filetime.days == 1):
                print(i, filetime.days)
                #os.remove(i)



# ---Loop counters
    loopcounterinput = loopcounterinput + 1
    loopcountermysql = loopcountermysql + 1
    loopcountertest = loopcountertest + 1

# ---Delay
    time.sleep(sleeptime)

# ---Beauty-Command
    os.system('clear')  # Disabele for Debug

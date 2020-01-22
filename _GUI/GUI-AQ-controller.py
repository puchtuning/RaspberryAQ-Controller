import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import GUI_ADMIN_AQ_controller as GUIADMIN

import time
import json
import logging


WIDTH = 800
HEIGHT = 600

H1 = ("Roboto", 24)
H2 = ("Roboto", 18)


BGFRAME = '#00DDFF'


aq_main_light_on = ""
aq_main_light_off = ""
aq_co2_on = ""
aq_co2_off = ""
aq_temp = ""



#--- Time Function
timestamp = time.strftime("%d.%m.%Y %H:%M:%S")
logtime = time.strftime("%Y-%m-%d")

#--- Logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename="../log/" + logtime + "_GUI-RaspberryAQ.log", level=logging.INFO)
logging.info('GUI-RaspberryAQ Started!')


#--- Click Funktionen
def clickecancel():
    logging.info('GUI-RaspberryAQ has been cosed.')
    app.destroy()


def clickedadmin():
    GUIADMIN.adminpage() 




##-- Starting the GUI
app = tk.Tk()

app.title("RaspberryAQ GUI")

canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH)
bgimage = tk.PhotoImage(file='_img/background.png')
bglabel = tk.Label(app, image=bgimage)
bglabel.place(bordermode='outside', relwidth=1, relheight=1)


canvas.pack()


##-- Dashboard

##--- Header
header = tk.Frame(app, bg=BGFRAME, bd=5)
header.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

title = tk.Label(header,anchor='center', text="RaspberryAQ-controller", bg=BGFRAME, bd=0, font=H1)
title.place(relwidth=1, relheight=1)

##--- Values

frameval = tk.Frame(app, bg=BGFRAME, bd=5)
frameval.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

title = tk.Label(header,anchor='center', text="RaspberryAQ-controller", bg=BGFRAME, bd=0, font=H1)
title.place(relwidth=1, relheight=1)


##--- Buttons

framebtn = tk.Frame(app, bg=BGFRAME, bd=5)
framebtn.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.1)

btnadmin = tk.Button(framebtn, text="Configure", bg="gray", fg="White", font=H2, command=clickedadmin)  # --Definiert ein Button
btnadmin.place(relwidth=0.49, relheight=1)  # --Definiert die Position des Buttons

btncancel = tk.Button(framebtn, text="Close", bg="gray", fg="White", font=H2, command=clickecancel)  # --Definiert ein Button
btncancel.place(relx=0.5, relwidth=0.49, relheight=1)  # --Definiert die Position des Buttons


app.mainloop()
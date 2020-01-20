import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename="log/" + logtime + "_GUI-RaspberryAQ.log", level=logging.INFO)
logging.info('GUI-RaspberryAQ Started!')


#--- Click Funktionen
def clickecancel():
    app.destroy()

#--- Check for Blanks
def is_not_blank(mystring, length):
    if(len(mystring) == length):
        print("")
    else:
        # Erstellt einen Error der durch die try Funktion gewertet erden kann
        raise ValueError('No Value specified')


    
#--- Starting Admin menu
def clickedadmin():

    def saveconfigfile():
        aq_main_light_on = txtadminl1.get()  # --Liest den Text aus dem txt1 aus
        aq_main_light_off = txtadminl2.get()
        aq_co2_on = txtadminc1.get()
        aq_co2_off = txtadminc2.get()
        aq_temp = spinadmint1.get()
        

        try:
            is_not_blank(aq_main_light_on, 5)
            is_not_blank(aq_main_light_off, 5)
            is_not_blank(aq_co2_on, 5)
            is_not_blank(aq_co2_off, 5)
            is_not_blank(aq_temp, 2)

            timestamp = time.strftime("%d.%m.%Y %H:%M:%S")

            # --Initialize JSON
            controllerinput = {}

            controllerinput["Controller-input"] = {  # Construct the input JSON file
                "timestamp": timestamp,
                "aq_main_light_on": aq_main_light_on,
                "aq_main_light_off": aq_main_light_off,
                "aq_co2_on": aq_co2_on,
                "aq_co2_off": aq_co2_off,
                "aq_temp": aq_temp
            }

            with open("data/_controller-input.json", 'w') as f:
                json.dump(controllerinput, f)

            print("Values written")
            logging.info('Values have been saved in JSON file')
            # shows info message
            messagebox.showinfo('Action successfull',
                                'Values written successfully')

        except ValueError:
            print("Values missing")
            logging.warning('Values could not be written')
            # shows warning message
            messagebox.showerror('Error: Falsche Werte', 'Eingabe Überprüfen')

    appadmin = tk.Toplevel()
    appadmin.title("Admin GUI")

    canvas = tk.Canvas(appadmin, height=HEIGHT, width=WIDTH, bg='gray')
    canvas.pack()
    header = tk.Frame(appadmin, bg=BGFRAME, bd=5)
    header.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    title = tk.Label(header,anchor='center', text="RaspberryAQ-controller", bg=BGFRAME, bd=0, font=H1)
    title.place(relwidth=1, relheight=1)
    
    ##--- Values

    frameval = tk.Frame(appadmin, bg=BGFRAME, bd=5)
    frameval.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    frameleft = tk.Frame(frameval, bg=BGFRAME)
    frameleft.pack(side='left', fill='both', padx=5, pady=5, expand=True)

    frameright = tk.Frame(frameval, bg=BGFRAME)
    frameright.pack(side='right', fill='both', padx=5, pady=5, expand=True)
    

    tk.Label(frameleft, anchor='w', text="Licht", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')
    tk.Label(frameleft, anchor='w', text="Einschaltzeit (z.B. 08:00):", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')
    tk.Label(frameleft, anchor='w', text="Ausschaltzeit (z.B. 22:00):", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')

    tk.Label(frameleft, anchor='w', text="CO2", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')
    tk.Label(frameleft, anchor='w', text="Einschaltzeit (z.B. 08:00):", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')
    tk.Label(frameleft, anchor='w', text="Ausschaltzeit (z.B. 22:00):", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')

    tk.Label(frameleft, anchor='w', text="Temperatur", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')
    tk.Label(frameleft, anchor='w', text="Wunschtemperatur (z.B. 25):", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')

    filler1 = tk.Label(frameright, text="", bg=BGFRAME, font=("Roboto", 18))
    txtadminl1 = tk.Entry(frameright, width=15, state='normal', font=H2)
    txtadminl2 = tk.Entry(frameright, width=15, state='normal', font=H2)

    filler2 = tk.Label(frameright, text="", bg=BGFRAME, font=("Roboto", 20))
    txtadminc1 = tk.Entry(frameright, width=15, state='normal', font=H2)
    txtadminc2 = tk.Entry(frameright, width=15, state='normal', font=H2)

    filler3 = tk.Label(frameright, text="", bg=BGFRAME, font=("Roboto", 19))
    spinadmint1 = tk.Spinbox(frameright, from_=15, to=40, width=5, font=H2)

    filler1.pack(padx=5, pady=5) #Filler
    txtadminl1.pack(padx=5, pady=5, fill='x')
    txtadminl2.pack(padx=5, pady=5, fill='x')
    filler2.pack(padx=5, pady=5) #Filler
    txtadminc1.pack(padx=5, pady=5, fill='x')
    txtadminc2.pack(padx=5, pady=5, fill='x')
    filler3.pack(padx=5, pady=5) #Filler
    spinadmint1.pack(padx=5, pady=5, fill='x')

    ##--- Buttons

    framebtn = tk.Frame(appadmin, bg=BGFRAME, bd=5)
    framebtn.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.1)

    btnadmin = tk.Button(framebtn, text="Save configfile", bg="gray", fg="White", font=H2, command=saveconfigfile)  # --Definiert ein Button
    btnadmin.place(relwidth=0.49, relheight=1)  # --Definiert die Position des Buttons

    btncancel = tk.Button(framebtn, text="Back", bg="gray", fg="White", font=H2, command= lambda: appadmin.destroy())  # --Definiert ein Button
    btncancel.place(relx=0.5, relwidth=0.49, relheight=1)  # --Definiert die Position des Buttons
        
    
    
    
    
    appadmin.mainloop()



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

btncancel = tk.Button(framebtn, text="Cancel", bg="gray", fg="White", font=H2, command=clickecancel)  # --Definiert ein Button
btncancel.place(relx=0.5, relwidth=0.49, relheight=1)  # --Definiert die Position des Buttons


app.mainloop()
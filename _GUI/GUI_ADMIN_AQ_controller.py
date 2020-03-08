import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import GUI_SAVEFILE as GUISAVE

import time
import json
import logging


WIDTH = 800
HEIGHT = 600

H1 = ("Roboto", 24)
H2 = ("Roboto", 18)


BGFRAME = '#00DDFF'




#--- Starting Admin menu
def adminpage():

    #---Opens window
    appadmin = tk.Toplevel()
    appadmin.title("Admin GUI")

    checkbtnval = tk.IntVar()

    def saveconfigfile():
        aq_main_light_on = txtadminl1.get()  # --Liest den Text aus dem txt1 aus
        aq_main_light_off = txtadminl2.get()
        aq_co2_on = txtadminc1.get()
        aq_co2_off = txtadminc2.get()
        aq_temp = spinadmint1.get()
        useMYSQL = bool(checkbtnval.get())


        

        try:
            GUISAVE.is_not_blank(aq_main_light_on, 5)
            GUISAVE.is_not_blank(aq_main_light_off, 5)
            GUISAVE.is_not_blank(aq_co2_on, 5)
            GUISAVE.is_not_blank(aq_co2_off, 5)
            GUISAVE.is_not_blank(aq_temp, 2)

            
            
            
            if(useMYSQL == True):
                HOST = txtmysql1.get() 
                DBNAME = txtmysql2.get() 
                USERNAME = txtmysql3.get() 
                PASSWD = txtmysql4.get()
                CONTROLLERID = txtmysql5.get()

                mysqlinput = {
                    "useMYSQL": useMYSQL,
                    "HOST": HOST,
                    "DBNAME": DBNAME,
                    "USERNAME": USERNAME, 
                    "PASSWD": PASSWD,
                    "CONTROLLERID": CONTROLLERID
                }
            else:
                mysqlinput ={
                    "useMYSQL": useMYSQL
                }   

            print(useMYSQL)            

            timestamp = time.strftime("%d.%m.%Y %H:%M:%S")

            # --Initialize JSON
            controllerinput = {}

            controllerinput["Controller-input"] = {  # Construct the input JSON file
                "timestamp": timestamp,
                "aq_main_light_on": aq_main_light_on,
                "aq_main_light_off": aq_main_light_off,
                "aq_co2_on": aq_co2_on,
                "aq_co2_off": aq_co2_off,
                "aq_temp": aq_temp,
                "MYSQL": mysqlinput
            }

            with open("../data/_controller-input.json", 'w') as f:
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


    def activateCheck():
        if (checkbtnval.get() == 1):
            txtmysql1.config(state='normal')
            txtmysql2.config(state='normal')  
            txtmysql3.config(state='normal')
            txtmysql4.config(state='normal')
            txtmysql5.config(state='normal')
        elif (checkbtnval.get() == 0):
            txtmysql1.config(state='disabled')
            txtmysql2.config(state='disabled')
            txtmysql3.config(state='disabled')
            txtmysql4.config(state='disabled')
            txtmysql5.config(state='disabled')


#---Tab control
    tab_control = ttk.Notebook(appadmin)

    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Admin')
    tab_control.pack(expand=1, fill='both')

    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='MYSQL')
    tab_control.pack(expand=1, fill='both')

    
#---Tab 1 Values

    canvas = tk.Canvas(tab1, height=HEIGHT, width=WIDTH, bg='gray')
    canvas.pack()
    header = tk.Frame(tab1, bg=BGFRAME, bd=5)
    header.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    title = tk.Label(header,anchor='center', text="RaspberryAQ-controller", bg=BGFRAME, bd=0, font=H1)
    title.place(relwidth=1, relheight=1)
    
    ##--- Values

    frameval = tk.Frame(tab1, bg=BGFRAME, bd=5)
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

    framebtn = tk.Frame(tab1, bg=BGFRAME, bd=5)
    framebtn.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.1)

    btnadmin = tk.Button(framebtn, text="Save configfile", bg="gray", fg="White", font=H2, command=saveconfigfile)  # --Definiert ein Button
    btnadmin.place(relwidth=0.49, relheight=1)  # --Definiert die Position des Buttons

    btncancel = tk.Button(framebtn, text="Back", bg="gray", fg="White", font=H2, command= lambda: appadmin.destroy())  # --Definiert ein Button
    btncancel.place(relx=0.5, relwidth=0.49, relheight=1)  # --Definiert die Position des Buttons


#---Tab 2 MYSQL

    canvas = tk.Canvas(tab2, height=HEIGHT, width=WIDTH, bg='gray')
    canvas.pack()
    header = tk.Frame(tab2, bg=BGFRAME, bd=5)
    header.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    title = tk.Label(header,anchor='center', text="MYSQL-connectror", bg=BGFRAME, bd=0, font=H1)
    title.place(relwidth=1, relheight=1)
    
    ##--- Values

    frameval = tk.Frame(tab2, bg=BGFRAME, bd=5)
    frameval.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    frameleft = tk.Frame(frameval, bg=BGFRAME)
    frameleft.pack(side='left', fill='both', padx=5, pady=5, expand=True)

    frameright = tk.Frame(frameval, bg=BGFRAME)
    frameright.pack(side='right', fill='both', padx=5, pady=5, expand=True)
    

    
    checkbtn = tk.Checkbutton(frameleft, text="Use MYSQL connector", variable=checkbtnval, command=activateCheck, offvalue=0, onvalue=1, bg=BGFRAME, font=H2)
    checkbtn.pack(padx=5, pady=5, fill='x')
    tk.Label(frameleft, anchor='w', text="MYSQL Host:", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')
    tk.Label(frameleft, anchor='w', text="Database Name:", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')    
    tk.Label(frameleft, anchor='w', text="Username:", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')
    tk.Label(frameleft, anchor='w', text="Password:", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')
    tk.Label(frameleft, anchor='w', text="Controller ID:", bg=BGFRAME, font=H2).pack(padx=5, pady=5, fill='x')

    
    

    filler1 = tk.Label(frameright, text="", bg=BGFRAME, font=("Roboto", 25))
    txtmysql1 = tk.Entry(frameright, width=15, state='normal', font=H2)
    txtmysql2 = tk.Entry(frameright, width=15, state='normal', font=H2)    
    txtmysql3 = tk.Entry(frameright, width=15, state='normal', font=H2)
    txtmysql4 = tk.Entry(frameright, width=15, state='normal', font=H2)
    txtmysql5 = tk.Entry(frameright, width=15, state='normal', font=H2)

    

    filler1.pack(padx=5, pady=5) #Filler
    txtmysql1.pack(padx=5, pady=5, fill='x')
    txtmysql2.pack(padx=5, pady=5, fill='x')    
    txtmysql3.pack(padx=5, pady=5, fill='x')
    txtmysql4.pack(padx=5, pady=5, fill='x')
    txtmysql5.pack(padx=5, pady=5, fill='x')


    ##--- Buttons

    framebtn = tk.Frame(tab2, bg=BGFRAME, bd=5)
    framebtn.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.1)

    btnadmin = tk.Button(framebtn, text="Save configfile", bg="gray", fg="White", font=H2, command=saveconfigfile)  # --Definiert ein Button
    btnadmin.place(relwidth=0.49, relheight=1)  # --Definiert die Position des Buttons

    btncancel = tk.Button(framebtn, text="Back", bg="gray", fg="White", font=H2, command= lambda: appadmin.destroy())  # --Definiert ein Button
    btncancel.place(relx=0.5, relwidth=0.49, relheight=1)  # --Definiert die Position des Buttons
        
    
    
    
    
    appadmin.mainloop()
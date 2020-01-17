from tkinter import Tk,Label,Entry,Button,Spinbox
from tkinter import ttk
from tkinter import messagebox
import os
import xml.etree.cElementTree as ET
import time



#---Time Function
timestamp = time.strftime("%d.%m.%Y %H:%M")


#--Check for Blanks
def is_not_blank(mystring,length):
    if(len(mystring) == length):
        error = "none"
    else:
        raise ValueError('No Value specified') #Erstellt einen Error der durch die try Funktion gewertet erden kann
    

#---Click Funktionen
def clicked():
    res = "Entry: " + txt1.get() #--Liest den Text aus dem txt1 aus
    lbl2.configure(text=res)

def clickecancel():
    window.destroy()

def clickedadmin():
    aq_main_light_on = txtadminl1.get() #--Liest den Text aus dem txt1 aus
    aq_main_light_off = txtadminl2.get()
    aq_co2_on = txtadminc1.get()
    aq_co2_off = txtadminc2.get()
    aq_temp = spinadmint1.get()

    
    try:
        is_not_blank(aq_main_light_on,5)
        is_not_blank(aq_main_light_off,5)
        is_not_blank(aq_co2_on,5)
        is_not_blank(aq_co2_off,5)
        is_not_blank(aq_temp,2)



        root = ET.Element("xml")
        doc = ET.SubElement(root, "controller-input")
        ET.SubElement(doc, "aq_main_light_on").text = aq_main_light_on
        ET.SubElement(doc, "aq_main_light_off").text = aq_main_light_off
        ET.SubElement(doc, "aq_co2_on").text = aq_co2_on
        ET.SubElement(doc, "aq_co2_off").text = aq_co2_off
        ET.SubElement(doc, "aq_temp").text = aq_temp
        ET.SubElement(doc, "written_at").text = timestamp


        tree = ET.ElementTree(root)
    
        tree.write("data\\" + "_controller-input.xml")
        
        print("Values written")
        messagebox.showinfo('Action successfull','Values written successfully') #shows info message

    except ValueError:
        print("Values missing")
        messagebox.showerror('Error: Falsche Werte', 'Eingabe Überprüfen')  #shows warning message

    
 
window = Tk() #--Startet Tkinter als window



 
window.title("Aquarium Controller GUI") #--Titel des Fensters
window.geometry('700x600') #--Definiert die Fenstergroesse

tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control) 
tab_control.add(tab1, text='Dashboard') 
tab_control.pack(expand=1, fill='both')

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Admin')
tab_control.pack(expand=1, fill='both')

##--- Tab Dashboard

lbl1 = Label(tab1, text="Aquarium Controller Dashboard" ,font=("Arial Bold", 20)) #--Definiert ein Textlable
lbl1.grid(column=0, row=0) #--Definiert die Position des Textlabels
lbl2 = Label(tab1, text="" ,font=("Arial Bold", 20))
lbl2.grid(column=0, row=2)

txt1 = Entry(tab1, width=10, state='normal') #--Defiiniert ein Eingabefeld/ mit State kann man das Texfeld aktivieren oder deaktivieren
txt1.focus() #--Setzt den Curser direkt in das Texfeld
txt1.grid(column=0, row=1)


btn1 = Button(tab1, text="Datenladen", bg="gray", fg="White", command=clicked) #--Definiert ein Button
btn1.grid(column=1, row=2) #--Definiert die Position des Buttons

##--- Tab Admin
lbladmin1 = Label(tab2, text="Aquarium Controller Admin", font=("Arial Bold", 20))

lbladminl1 = Label(tab2, text="Licht", font=("Arial", 10))
lbladminl2 = Label(tab2, text="Einschaltzeit (z.B. 08:00):", font=("Arial", 10))
lbladminl3 = Label(tab2, text="Ausschaltzeit (z.B. 22:00):", font=("Arial", 10))

lbladminc1 = Label(tab2, text="CO2", font=("Arial", 10))
lbladminc2 = Label(tab2, text="Einschaltzeit (z.B. 08:00):", font=("Arial", 10))
lbladminc3 = Label(tab2, text="Ausschaltzeit (z.B. 22:00):", font=("Arial", 10))

lbladmint1 = Label(tab2, text="Temperatur", font=("Arial", 10))
lbladmint2 = Label(tab2, text="Wunschtemperatur (z.B. 25):", font=("Arial", 10))

txtadminl1 = Entry(tab2, width=15, state='normal')
txtadminl2 = Entry(tab2, width=15, state='normal')

txtadminc1 = Entry(tab2, width=15, state='normal')
txtadminc2 = Entry(tab2, width=15, state='normal')

spinadmint1 = Spinbox(tab2, from_=15, to=40, width=5)


lbladmin1.grid(column=0, row=0)

lbladminl1.grid(column=0, row=1)
lbladminl2.grid(column=0, row=2)
txtadminl1.grid(column=1, row=2)
lbladminl3.grid(column=0, row=3)
txtadminl2.grid(column=1, row=3)

lbladminc1.grid(column=0, row=4)
lbladminc2.grid(column=0, row=5)
txtadminc1.grid(column=1, row=5)
lbladminc3.grid(column=0, row=6)
txtadminc2.grid(column=1, row=6)

lbladmint1.grid(column=0, row=7)
lbladmint2.grid(column=0, row=8)
spinadmint1.grid(column=1, row=8)

##-- Buttons

lblsubmit = Label(tab2, text=" ", font=("Arial", 10))
lblsubmit.grid(column=1, row=10)

btnadmin1 = Button(tab2, text="Config File Schreiben", bg="gray", fg="White", command=clickedadmin) #--Definiert ein Button
btnadmin1.grid(column=1, row=11) #--Definiert die Position des Buttons

btnadmin2 = Button(tab2, text="Cancel", bg="gray", fg="White", command=clickecancel) #--Definiert ein Button
btnadmin2.grid(column=2, row=11) #--Definiert die Position des Buttons



window.mainloop()
import customtkinter
import tkinter as tk
from tkinter import ttk
import tkinter
import pymysql
from subprocess import call
from tkinter import messagebox
import ctypes
from PIL import ImageTk, Image
from PIL import Image
import mysql.connector
import customtkinter as ctk

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jms0246",
    database="HospitalManagement"
)

def search_prescription():
    if e1.get()=="":
        messagebox.showerror('Error','Fields cannot be empty')
    else:
        patient_name = e1.get()
        if patient_name:
            # Execute SQL query
            cursor = db.cursor()
            cursor.execute("SELECT Prescription FROM Patient11 WHERE PatientName = %s", (patient_name,))
            result = cursor.fetchone()

            if result:
                # Show prescription in a new window
                prescription_window = tk.Toplevel(root)
                prescription_window.title("Prescription")

                prescription_label = ctk.CTkLabel(prescription_window, text=result[0], wraplength=400,text_color="black")
                prescription_label.pack(padx=20, pady=20)
            else:
                messagebox.showerror("Error", "Patient not found!")
        else:
            messagebox.showwarning("Warning", "Please enter the patient's name.")


def search():

    return

def back():
    root.destroy()


root=customtkinter.CTk()
root.geometry("1520x700+0+0")





img2=customtkinter.CTkImage(dark_image=Image.open("bag.jpg"),light_image=Image.open("bag.jpg"),size=(1500,700))

l4=customtkinter.CTkLabel(master=root,image=img2,width=1500,height=700,bg_color="cyan",text=None)   #(900,610),
l4.place(relx=0,rely=0)

e1=customtkinter.CTkEntry(master=root,width=500,height=40,placeholder_text="Search Patient",font=('century gothic',20))
e1.place(x=400,y=300)


frame1=customtkinter.CTkFrame(master=root,width=700,height=100,bg_color="blue",fg_color="blue")
frame1.place(x=300,y=10)

my_label2=customtkinter.CTkLabel(master=frame1,text='Prescription',font=('century gothic',60,'bold'))
my_label2.place(x=200, y=10)

button1=customtkinter.CTkButton(master=root,text="Search",width=220,height=40,command=search_prescription)
button1.place(x=400,y=400)

button2=customtkinter.CTkButton(master=root,text="Back",width=220,height=40,command=back)
button2.place(x=700,y=400)


root.mainloop()
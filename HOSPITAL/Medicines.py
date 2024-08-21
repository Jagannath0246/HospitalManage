import customtkinter
from PIL import Image
import mysql.connector
import pymysql
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


def search_quantity():
    # Get the medicine name from the entry widget
    medicine_name = e1.get()

    if not medicine_name:
        messagebox.showwarning("Warning", "Please enter the medicine name.")
        return

    try:
        # Connect to the MySQL database
        with mysql.connector.connect(
            host="localhost",
            user="root",
            password="jms0246",
            database="HospitalManagement"
        ) as db:
            # Create a cursor object
            cursor = db.cursor()

            # Execute the SQL query to retrieve the quantity of the medicine
            cursor.execute("SELECT Quantity FROM Medicines2 WHERE Name = %s", (medicine_name,))
            result = cursor.fetchone()

            if result:
                # If the medicine is found, display the available quantity in a new window
                quantity_window = tk.Toplevel(root)
                quantity_window.title("Available Quantity")

                # Create a label to display the available quantity
                quantity_label = ctk.CTkLabel(quantity_window, text=f"Available Quantity of {medicine_name}: {result[0]}",text_color="black")
                quantity_label.pack(padx=20, pady=20)
            else:
                messagebox.showerror("Error", "Medicine not found!")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error accessing database: {e}")
    return


def clear_entry():
    # Clear the medicine name entry
    e1.delete(0, tk.END)


#my_image=customtkinter.CTkImage(light_image=Image.open('images/Image12.jpg'),dark_image=Image.open('images/Image12.jpg'),size=(1500,700))

#my_label=customtkinter.CTkLabel(root,text="",image=my_image)
#my_label.pack()
# def insert():
#     connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="student",
#     database="Medicines2"
#     )
#     cursor = connection.cursor()

#     query="SELECT * from Medicines2"

#     Medicines3=e1.get()
#     connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',databse='HospitalManagement')
    
#     c=connection.cursor()
#     c.execute("Select Name from Medicine2 where Name=%s;",(Medicines3,))
#     data = c.fetchall()
    
#     value = [item[0] for item in data]
#     connection.commit()

root=customtkinter.CTk()
root.geometry("1520x700+0+0")

img2=customtkinter.CTkImage(dark_image=Image.open("xc.jpg"),light_image=Image.open("xc.jpg"),size=(1500,700))

l4=customtkinter.CTkLabel(master=root,image=img2,width=1500,height=700,bg_color="cyan",text=None)   #(900,610),
l4.place(relx=0,rely=0)

e1=customtkinter.CTkEntry(master=root,width=500,height=40,placeholder_text="Search Medicine",font=('century gothic',20))
e1.place(x=400,y=300)


frame1=customtkinter.CTkFrame(master=root,width=700,height=100,fg_color="blue")
frame1.place(x=300,y=10)

my_label2=customtkinter.CTkLabel(master=frame1,text='MEDICINES',font=('century gothic',60,'bold'))
my_label2.place(x=200, y=10)

button1=customtkinter.CTkButton(master=root,text="Search",width=220,height=40,command=search_quantity)
button1.place(x=400,y=400)

button2=customtkinter.CTkButton(master=root,text="Back",width=220,height=40,command=exit)
button2.place(x=700,y=400)






root.mainloop()
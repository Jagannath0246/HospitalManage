import tkinter
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
#from tkinter import *
from subprocess import call
import smtplib
import random
from twilio.rest import Client
import mysql.connector

def asd():
    app.destroy()

    call(['python','forgot.py'])

# def www():

#     import main

def email_log():
    app.destroy()
    call(['python','otp1.py'])

#REC CODE
#1CTFTWGKE4DJX7N5BUJ1PUZL

def otp():
    otp=random.randint(1000,9999)

    account_sid="AC4c13fefaf64b2e2fc14de9dfdb0c1acb"

    auth_token="bed980b0384e627b472600e4a580bfc5"

    client=Client(account_sid,auth_token)

    msg=client.messages.create(
        body=f"Your OtP is {otp}",
        from_="+17179644665",
        to = "+919022414773")
    print(otp)


def login():
    if box1.get()=='' or box2.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')

    elif box1.get()=='admin' and box2.get()=='12345':
        messagebox.showinfo('Success','Welcome')
        app.destroy()
        call(['python','main.py'])


    elif box1.get()!='admin' or box2.get()!='12345':
        messagebox.showerror('Error','Incorrect User ID or Password')



def validate_login(username, password):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jms0246",
            database="HospitalManagement"
        )
        cursor = connection.cursor()

        # Query to check if the username and password match
        query = "SELECT * FROM Users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        # Close the database connection
        cursor.close()
        connection.close()

        return result is not None
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return False


# Function to handle login button click event
def login_clicked():
    username = box1.get()
    password = box2.get()
    if validate_login(username, password):
        if btn1.get()==1:

            # Login successful, display message
            messagebox.showinfo('Success','Welcome')
            app.destroy()
            call(['python','main.py'])
        else:
            messagebox.showerror('Error','agree to terms and conditions')
    elif box1.get()=='' or box2.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    else:
        # Login failed, display error message
        messagebox.showerror('Error','Invalid username or password')




#_____________________________________appreances___________________________________________________________________
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#______________________________________window for login____________________________________________________________
app=customtkinter.CTk()
app.geometry("600x440+500+200")

app.title("LOGIN")


#---------------------------------------BG Image-------------------------------------------------------------------
img2=customtkinter.CTkImage(light_image=Image.open("logbg.jpg"),dark_image=Image.open("logbg.jpg"),size=(600,440))

# img1=ImageTk.PhotoImage(Image.open("logbg.jpg"))
l1=customtkinter.CTkLabel(master=app,image=img2)
l1.pack()

#---------------------------------------------Frame mini _--------------------------------------------------------
Frame1=customtkinter.CTkFrame(master=l1,width=320,height=360,corner_radius=15,border_width=5,border_color="cyan")
Frame1.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)

#---------------------------------------------label ----------------------------------------------------------

#width=,height=,corner_radius=,bg_color="Transparent"
l2=customtkinter.CTkLabel(master=Frame1,text="Log in into your Account",font=('Century Gothic',20))
l2.place(x=40,y=45)

#--------------------------------------------text box/entry---------------------------------------------------
box1=customtkinter.CTkEntry(master=Frame1,width=220,placeholder_text="Username...")
box1.place(x=50,y=110)

box2=customtkinter.CTkEntry(master=Frame1,width=220,placeholder_text="Password...",show="*")
box2.place(x=50,y=165)


btn1=customtkinter.CTkSwitch(master=Frame1,text="Agree to Terms & Conditions",font=('Century Gothic',10),switch_height=15,switch_width=30,corner_radius=20,progress_color="cyan")
btn1.place(x=85,y=300)


btn2=customtkinter.CTkButton(master=Frame1,text="Login",corner_radius=6,border_color="cyan",fg_color="transparent",border_width=3,hover_color="darkblue",command=login_clicked)
btn2.place(x=50,y=240)

btn3=customtkinter.CTkSwitch(master=Frame1,text="Forgot password",font=('Century Gothic',10),switch_height=15
                             ,switch_width=30,corner_radius=20,progress_color="cyan",command=asd)
# btn3=customtkinter.CTkCheckBox(master=Frame1,text="Forgot Password")
btn3.place(x=155,y=195)

app.mainloop()
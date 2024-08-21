import tkinter
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
# from tkinter import *


#_____________________________________appreances___________________________________________________________________
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#______________________________________window for login____________________________________________________________
app=customtkinter.CTk()
app.geometry("600x440+500+200")

app.title("LOGIN")


#---------------------------------------BG Image-------------------------------------------------------------------
# img2=customtkinter.CTkImage(light_image=Image.open("logbg.jpg"),dark_image=Image.open("logbg.jpg"),size=(600,440))


img1=ImageTk.PhotoImage(Image.open("logbg.jpg"))
l1=customtkinter.CTkLabel(master=app,image=img1)
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

box2=customtkinter.CTkEntry(master=Frame1,width=220,placeholder_text="Password...")
box2.place(x=50,y=165)


# l3=customtkinter.CTkLabel(master=Frame1,text="Forgot Password",font=('Century Gothic',12))
# l3.place(x=155,y=195)


# l4=customtkinter.CTkLabel(master=Frame1,text="Agree to Terms & Conditions",font=('Century Gothic',10))
# l4.place(x=100,y=300)

#,radiobutton_width=20,radiobutton_height=20

btn1=customtkinter.CTkSwitch(master=Frame1,text="Agree to Terms & Conditions",font=('Century Gothic',10),switch_height=15,switch_width=30,corner_radius=20,progress_color="cyan")
btn1.place(x=85,y=300)

# l5=customtkinter.CTkLabel(master=Frame1,text="Forgot Password",font=('Century Gothic',12))
# l5.place(x=155,y=195)        ,height=15,width=30       height=15,width=100, font=('Botthanie',20),

# btn2=customtkinter.CTkButton(master=Frame1,text="Login",corner_radius=6,border_color="cyan",fg_color="transparent",border_width=3,hover_color="darkblue",command=login)
# btn2.place(x=50,y=240)



btn3=customtkinter.CTkSwitch(master=Frame1,text="Forgot password",font=('Century Gothic',10),switch_height=15
                             ,switch_width=30,corner_radius=20,progress_color="cyan")
# btn3=customtkinter.CTkCheckBox(master=Frame1,text="Forgot Password")
btn3.place(x=155,y=195)








app.mainloop()
import tkinter
# from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from subprocess import call

def back():

    wap.destroy()
    call(['python','main.py'])

#_____________________________________appreances___________________________________________________________________
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


#______________________________________window for add patient______________________________________________________
wap=customtkinter.CTk()
wap.geometry("1520x700+0+0")
wap.title("Hospital")

l2=tkinter.Label(wap,bd=20,relief="ridge",text="+ Hospital Management System +",fg="cyan",bg="darkblue",font=("times new roman",50,"bold"))
l2.pack(side="top",fill="x")


img2=customtkinter.CTkImage(dark_image=Image.open("aapp.jpg"),light_image=Image.open("aapp.jpg"),size=(1500,610))

l4=customtkinter.CTkLabel(master=wap,image=img2,width=1500,height=610,bg_color="cyan",text=None)   #(900,610),
l4.place(relx=0,rely=0.115)


















btn2=customtkinter.CTkButton(master=wap,text="Go Back",corner_radius=6,border_color="RED",fg_color="red",border_width=3,hover_color="RED",command=back)
btn2.place(relx=0.86,rely=0.9)
wap.mainloop()


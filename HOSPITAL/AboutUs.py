import tkinter
# from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from subprocess import call


def back():
    uap.destroy()
    call(['python','main.py'])

#_____________________________________appreances___________________________________________________________________
customtkinter.set_appearance_mode("light")



#______________________________________window for add patient______________________________________________________
uap=customtkinter.CTk()
uap.geometry("1520x700+0+0")
uap.title("Hospital")

l2=tkinter.Label(uap,bd=20,relief="ridge",text="+ Hospital Management System +",fg="cyan",bg="darkblue",font=("times new roman",50,"bold"))
l2.pack(side="top",fill="x")


img2=customtkinter.CTkImage(dark_image=Image.open("aapp.jpg"),light_image=Image.open("aapp.jpg"),size=(1500,610))

l4=customtkinter.CTkLabel(master=uap,image=img2,width=1500,height=610,bg_color="cyan",text=None)   #(900,610),
l4.place(relx=0,rely=0.115)


# frame1=customtkinter.CTkFrame(master=)


Frame2=customtkinter.CTkFrame(master=uap,width=600,height=500,corner_radius=15,border_width=5,border_color="cyan",bg_color="cyan",fg_color="white")
Frame2.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)

# l6=customtkinter.CTkLabel(master=Frame2,text="Name:Jagannath Mahadev Sarmalkar",text_color="black",font=("times new roman",20,"bold"),fg_color="transparent",bg_color="transparent",corner_radius=15)
# l6.place(x=10,y=10)
# l7=customtkinter.CTkLabel(master=Frame2,text="Roll No: 62",text_color="black",font=("times new roman",20,"bold"),fg_color="transparent",bg_color="transparent",corner_radius=15)
# l7.place(x=10,y=40)
# l8=customtkinter.CTkLabel(master=Frame2,text="Name:Gandhar Nilesh Thatte",text_color="black",font=("times new roman",20,"bold"),fg_color="transparent",bg_color="transparent",corner_radius=15)
# l8.place(x=10,y=70)
# l8=customtkinter.CTkLabel(master=Frame2,text="Roll No: 68",text_color="black",font=("times new roman",20,"bold"),fg_color="transparent",bg_color="transparent",corner_radius=15)
# l8.place(x=10,y=100)


l6=customtkinter.CTkLabel(master=Frame2,text="Address : Mirjole Ratnagiri",text_color="black",font=("times new roman",20,"bold"),fg_color="transparent",bg_color="transparent",corner_radius=15)
l6.place(x=10,y=10)
l7=customtkinter.CTkLabel(master=Frame2,text="Contact : 7796100349",text_color="black",font=("times new roman",20,"bold"),fg_color="transparent",bg_color="transparent",corner_radius=15)
l7.place(x=10,y=40)
l8=customtkinter.CTkLabel(master=Frame2,text="Email : quantumcure@gmail.com",text_color="black",font=("times new roman",20,"bold"),fg_color="transparent",bg_color="transparent",corner_radius=15)
l8.place(x=10,y=70)








btn2=customtkinter.CTkButton(master=uap,text="Go Back",corner_radius=6,border_color="RED",fg_color="red",border_width=3,hover_color="RED",command=back)
btn2.place(relx=0.86,rely=0.9)
uap.mainloop()


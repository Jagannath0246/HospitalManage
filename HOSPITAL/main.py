import tkinter
# from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
from subprocess import call


def AddPatient():
    tap.destroy()
    call(['python','AddPatient.py'])

def AboutUs():
    tap.destroy()
    call(['python','AboutUs.py'])

def EmployeeInfo():
    tap.destroy()
    call(['python','EmployeeInfo.py'])

def PatientInfo():
    tap.destroy()
    call(['python','PatientInfo.py'])

def Services():
    tap.destroy()
    call(['python','Project1.py'])

def AddEmployee():
    tap.destroy()
    call(['python','AddEmployee.py'])

def login():
    tap.destroy()
    call(['python','login.py'])


#_____________________________________appreances___________________________________________________________________
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#______________________________________window for login____________________________________________________________
tap=customtkinter.CTk()
tap.geometry("1520x700+0+0")

# img1=ImageTk.PhotoImage(Image.open("aapp.jpg"))
# l1=customtkinter.CTkLabel(master=app,image=img1)
# l1.pack()

tap.title("Hospital")

l2=tkinter.Label(tap,bd=20,relief="ridge",text="+ QuantumCare Hospital +",fg="cyan",bg="darkblue",font=("times new roman",50,"bold"))
l2.pack(side="top",fill="x")

# l3=tkinter.Label(tap,bd=20,relief="ridge",fg="cyan",bg="#480f61",font=("times new roman",50,"bold"),width=15)
# l3.pack(side="left",fill="y")

img2=customtkinter.CTkImage(dark_image=Image.open("a2.jpg"),light_image=Image.open("a2.jpg"),size=(1500,610))

l4=customtkinter.CTkLabel(master=tap,image=img2,width=1500,height=610,bg_color="cyan",text=None)   #(900,610),
l4.place(relx=0,rely=0.115)


btn1=customtkinter.CTkButton(master=l4,text="Add Employee",corner_radius=6,border_color="black",fg_color="blue",bg_color="transparent",border_width=3,hover_color="red",font=("times new roman",20,"bold"),width=200,command=AddEmployee)
btn1.place(x=50,y=180)

btn2=customtkinter.CTkButton(master=l4,text="Employee Information",corner_radius=6,border_color="black",fg_color="blue",bg_color="transparent",border_width=3,hover_color="red",font=("times new roman",20,"bold"),width=200,command=EmployeeInfo)
btn2.place(x=50,y=240)

btn3=customtkinter.CTkButton(master=l4,text="Add Patient",corner_radius=6,border_color="black",fg_color="blue",bg_color="transparent",border_width=3,hover_color="red",font=("times new roman",20,"bold"),width=200,command=AddPatient)
btn3.place(x=50,y=60)


btn4=customtkinter.CTkButton(master=l4,text="Patient Information",corner_radius=6,border_color="black",fg_color="blue",bg_color="transparent",border_width=3,hover_color="red",font=("times new roman",20,"bold"),width=200,command=PatientInfo)
btn4.place(x=50,y=120)


btn5=customtkinter.CTkButton(master=l4,text="Pharmacy",corner_radius=6,border_color="black",fg_color="blue",bg_color="transparent",border_width=3,hover_color="red",font=("times new roman",20,"bold"),width=200,command=Services)
btn5.place(x=50,y=300)

btn6=customtkinter.CTkButton(master=l4,text="About Us",corner_radius=6,border_color="black",fg_color="blue",bg_color="transparent",border_width=3,hover_color="red",font=("times new roman",20,"bold"),width=200,command=AboutUs)
btn6.place(x=50,y=360)

btn7=customtkinter.CTkButton(master=l4,text="To Login Page",corner_radius=6,border_color="black",fg_color="#480f61",bg_color="transparent",border_width=3,hover_color="red",font=("times new roman",20,"bold"),width=200,command=login)
btn7.place(x=50,y=420)

btn7=customtkinter.CTkButton(master=l4,text="Exit",corner_radius=6,border_color="black",fg_color="transparent",bg_color="transparent",border_width=3,hover_color="red",font=("times new roman",20,"bold"),width=200,command=tap.destroy)
btn7.place(x=50,y=480)













tap.mainloop()
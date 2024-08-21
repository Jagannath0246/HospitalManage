import tkinter
from customtkinter import *
# from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from subprocess import call
import mysql.connector
# import mysql.connector as c
import random

def random_num():
    return random.randint(1000,9999)



def insert():
    PatientId=random_num()
    PatientName=l7.get()
    DateOfBirth=l10.get()
    Address=l12.get()
    Diagnosis=l14.get()
    FatherName=l16.get()
    MotherName=l19.get()
    BloodGroup=l21.get()
    PhoneNumber=l23.get()
    Prescription=l25.get("1.0", "end-1c")

    connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
    c=connection.cursor()

    # insert_query ="INSERT INTO college1 ('PatientId','PatientName','DateOfBirth','Address','Diagnosis','NameOfTablet','NoOfTablet','Issuedate','ExpiryDate') VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    # vals=(PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate)
    # c.execute("insert into college1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PatientId,PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate))
    c.execute("insert into Patient9 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PatientId,PatientName,DateOfBirth,Address,Diagnosis,FatherName,MotherName,BloodGroup,PhoneNumber,Prescription))
    connection.commit()
    # c.commit()
    # c.close()
    return




def back():
    dap.destroy()
    call(['python','main.py'])



#_____________________________________appreances___________________________________________________________________
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


#______________________________________window for add patient______________________________________________________
dap=customtkinter.CTk()
dap.geometry("1520x700+0+0")

dap.title("Hospital")

l2=tkinter.Label(dap,bd=20,relief="ridge",text="+ Hospital Management System +",fg="cyan",bg="darkblue",font=("times new roman",50,"bold"))
l2.pack(side="top",fill="x")

img2=customtkinter.CTkImage(dark_image=Image.open("aapp.jpg"),light_image=Image.open("aapp.jpg"),size=(1500,610))

l4=customtkinter.CTkLabel(master=dap,image=img2,width=1500,height=610,bg_color="cyan",text=None)   #(900,610),
l4.place(relx=0,rely=0.115)

l5=tkinter.Label(dap,bd=20,relief="ridge",fg="cyan",bg="#cfe2f3",font=("times new roman",50,"bold"),width=47,height=12)
l5.place(relx=0,rely=0.11)

#---------------------------------------------label ----------------------------------------------------------

#width=,height=,corner_radius=,bg_color="Transparent"
l3=customtkinter.CTkLabel(master=l5,text="Patient ID",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l3.place(x=40,y=45)

l6=customtkinter.CTkLabel(master=l5,text=str(random_num()),text_color="black",font=("times new roman",20,"bold"),fg_color="#e1dfcf",bg_color="#cfe2f3",corner_radius=6,width=400)
l6.place(x=345,y=45)

l9=customtkinter.CTkLabel(master=l5,text="Patient Name",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l9.place(x=40,y=105)

l7=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#cfe2f3",border_color="black",border_width=4,corner_radius=15)
l7.place(x=345,y=105)

l8=customtkinter.CTkLabel(master=l5,text="Date Of Birth",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l8.place(x=40,y=165)

l10=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#cfe2f3",border_color="black",border_width=4,corner_radius=15)
l10.place(x=345,y=165)

l11=customtkinter.CTkLabel(master=l5,text="Address",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l11.place(x=40,y=225)

l12=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#cfe2f3",border_color="black",border_width=4,corner_radius=15)
l12.place(x=345,y=225)

l13=customtkinter.CTkLabel(master=l5,text="Diagnosis",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l13.place(x=40,y=285)

l14=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#cfe2f3",border_color="black",border_width=4,corner_radius=15)
l14.place(x=345,y=285)

# lblNameTablet=tkinter.Label(l5,text="Names Of Tablets",font=("times new roman",12,"bold"),padx=2,pady=6)
# lblNameTablet.grid(row=0,column=0)

# comNameTablet=ttk.Combobox(l5,font=("times new roman",12,"bold"),
#                                                             width=70,height=80)Dopamine
# Doxazosin
# Doxepin
# Doxorubicin
# comNameTablet["values"]=("Ativan","Cymbalta","Otezla","Viagra","Boldcare","Bangali@Baba")
# comNameTablet.place(x=525,y=500)

# =customtkinter.CTkComboBox(master=l5,values=["Ativan","Cymbalta","Otezla","Dopamine","Doxazosin","Doxepin","Doxorubicin"],width=400)

l16=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#cfe2f3",border_color="black",border_width=4,corner_radius=15)
l16.place(x=345,y=345)

l17=customtkinter.CTkLabel(master=l5,text="Father Name",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l17.place(x=40,y=345)

# l18=customtkinter.CTkSlider(master=l5,from_=3,to=30,number_of_steps=10)
# l18.place(x=345,y=405)

l18=customtkinter.CTkLabel(master=l5,text="Mother Name",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l18.place(x=40,y=405)


l19=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#cfe2f3",border_color="black",border_width=4,corner_radius=15)
l19.place(x=345,y=405)


l20=customtkinter.CTkLabel(master=l5,text="Blood Group",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l20.place(x=40,y=465)


l21=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#cfe2f3",border_color="black",border_width=4,corner_radius=15)
l21.place(x=345,y=465)


l22=customtkinter.CTkLabel(master=l5,text="Phone Number",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l22.place(x=40,y=525)


l23=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#cfe2f3",border_color="black",border_width=4,corner_radius=15)
l23.place(x=345,y=525)


l26=customtkinter.CTkLabel(master=l5,text="Prescription :",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l26.place(x=900,y=40)

l25=CTkTextbox(l5,font=("times new roman",12,"bold"),width=300,height=340,border_width=2,border_color="black",scrollbar_button_color="grey")#,padx=2,pady=6)
l25.place(x=900,y=100)










btn2=customtkinter.CTkButton(master=l5,text="Go Back",text_color="black",corner_radius=6,border_color="RED",fg_color="transparent",border_width=3,hover_color="RED",command=back)
btn2.place(relx=0.86,rely=0.9)

btn3=customtkinter.CTkButton(master=l5,text="Confirm",text_color="black",corner_radius=6,border_color="light green",fg_color="transparent",border_width=3,hover_color="light green",command=insert)
btn3.place(relx=0.73,rely=0.9)



dap.mainloop()
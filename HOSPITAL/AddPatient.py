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
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage

from PIL import Image, ImageTk

def random_num():
    return random.randint(1000,9999)

def view_document():
    document_path = l30.get()
    if document_path:
        # Open the image and convert it to PNG format
        with Image.open(document_path) as img:
            img_png = img.convert("RGB")
            img_png.save("converted_image.png", format="PNG")

        # Open a new window to display the image
        new_window = tk.Toplevel(dap)
        new_window.title("View Document")
        new_window.geometry("1900x1400+0+0")

        # Load the converted image
        image = ImageTk.PhotoImage(file="converted_image.png")

        # Display the image in a label
        image_label = tk.Label(new_window, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack()

def upload_document():
    filename = filedialog.askopenfilename(title="Select a document")
    if filename:
        # Display the filename in the entry widget
        l30.insert(0, filename)

def insert():
    if l7.get()=='' or l10.get()=='' or l12.get()=='' or l14.get()=='' or l16.get()=='' or l19.get()=='' or l21.get()=='' or l23.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    else:
        BloodGroup=l21.get()
        valid_blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if BloodGroup in valid_blood_groups:
            print("success")
        else:
            messagebox.showerror("Validation Error", "Please enter a valid blood group.")
            return
        PhoneNumber=l23.get()
        if PhoneNumber.isdigit() and len(PhoneNumber) == 10:
            print("success")

        else:
            messagebox.showerror("Validation Error", "Please enter a 10-digit integer phone number.")
            return
        PatientId=random_num()
        PatientName=l7.get()
        DateOfBirth=l10.get()
        Address=l12.get()
        Diagnosis=l14.get()
        FatherName=l16.get()
        MotherName=l19.get()


        Prescription=l25.get("1.0", "end-1c")
        Photo=str(l30.get())

        connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
        c=connection.cursor()

        # insert_query ="INSERT INTO college1 ('PatientId','PatientName','DateOfBirth','Address','Diagnosis','NameOfTablet','NoOfTablet','Issuedate','ExpiryDate') VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    # vals=(PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate)
    # c.execute("insert into college1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PatientId,PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate))
        c.execute("insert into Patient11 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PatientId,PatientName,DateOfBirth,Address,Diagnosis,FatherName,MotherName,BloodGroup,PhoneNumber,Prescription,Photo))
        connection.commit()
        # c.commit()
        # c.close()
        messagebox.showinfo('Success','Patient Registered Successfully')
        return


def photo():
    Pic=l30.get()
    img2 = customtkinter.CTkImage(dark_image=Image.open(l30.get()), light_image=Image.open(l30.get()), size=(188,155))
    l31 = customtkinter.CTkLabel(master=l32, image=img2, width=185, height=155, bg_color="cyan", text=None)
    l31.place(x=0, y=0)
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

l2=tkinter.Label(dap,bd=20,relief="ridge",text="+ QuantumCare Hospital +",fg="cyan",bg="darkblue",font=("times new roman",50,"bold"))
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
l26.place(x=900,y=320)

l25=CTkTextbox(l5,font=("times new roman",12,"bold"),width=300,height=180,border_width=2,border_color="black",scrollbar_button_color="grey")#,padx=2,pady=6)
l25.place(x=900,y=350)

l33=customtkinter.CTkLabel(master=l5,text="Photo :",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l33.place(x=900,y=200)

l30=customtkinter.CTkEntry(master=l5,placeholder_text="Enter Image Name...",font=("times new roman",20,"bold"),fg_color="white",width=300,bg_color="#cfe2f3",border_color="black",border_width=4,corner_radius=15)
l30.place(x=900,y=230)

l32=tkinter.Label(l5,bd=20,relief="ridge",fg="cyan",bg="#906be4",font=("times new roman",50,"bold"),width=7,height=3)
l32.place(x=1400,y=10)
#906be4
#00b6bc
#002f9b

btn4=customtkinter.CTkButton(master=l5,text="Upload",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=upload_document)
btn4.place(relx=0.72,rely=0.45)

btn5=customtkinter.CTkButton(master=l5,text="View Image",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=photo)
btn5.place(relx=0.85,rely=0.45)



btn2=customtkinter.CTkButton(master=l5,text="Go Back",text_color="black",corner_radius=6,border_color="RED",fg_color="transparent",border_width=3,hover_color="RED",command=back)
btn2.place(relx=0.86,rely=0.9)

btn3=customtkinter.CTkButton(master=l5,text="Confirm",text_color="black",corner_radius=6,border_color="light green",fg_color="transparent",border_width=3,hover_color="light green",command=insert)
btn3.place(relx=0.73,rely=0.9)



dap.mainloop()






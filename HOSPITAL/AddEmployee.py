import tkinter
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


def back():

    qap.destroy()
    call(['python','main.py'])

def view_document():
    document_path = l30.get()
    if document_path:
        # Open the image and convert it to PNG format
        with Image.open(document_path) as img:
            img_png = img.convert("RGB")
            img_png.save("converted_image.png", format="PNG")

        # Open a new window to display the image
        new_window = tk.Toplevel(qap)
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



""" not in use
def confirm():
    if l7.get()=='' or l10.get()=='' or l12.get()=='' or l14.get()=='' or l16.get()=='' or l19.get()=='' or l21.get()=='' or l23.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    else:
        def insert():
            EmployeeId =random_num()
            EmployeeName=l7.get()
            DateOfBirth=l10.get()
            Address=l12.get()
            Qualification=l14.get()
            Department=l16.get()
            Salary=str(l19.get())
            JoiningDate=l21.get()
            PhoneNumber=str(l23.get())

            connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
            c=connection.cursor()

    # insert_query ="INSERT INTO college1 ('PatientId','PatientName','DateOfBirth','Address','Diagnosis','NameOfTablet','NoOfTablet','Issuedate','ExpiryDate') VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    # vals=(PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate)
    # c.execute("insert into college1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PatientId,PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate))
            c.execute("insert into Employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(EmployeeId,EmployeeName,DateOfBirth,Address,Qualification,Department,Salary,JoiningDate,PhoneNumber))
            connection.commit()
    # c.commit()
    # c.close()
            return
        # messagebox.showinfo('Success','Welcome')
    return
"""

def photo():
    Pic=l30.get()
    img2 = customtkinter.CTkImage(dark_image=Image.open(Pic), light_image=Image.open(Pic), size=(188,155))
    l31 = customtkinter.CTkLabel(master=l32, image=img2, width=185, height=155, bg_color="cyan", text=None)
    l31.place(x=0, y=0)
    return


def random_num():
    return random.randint(10000,99999)

def insert():
    messagebox.showinfo('Notice','Employee Registered Successfully')
    if l7.get()=='' or l10.get()=='' or l12.get()=='' or l14.get()=='' or l16.get()=='' or l19.get()=='' or l21.get()=='' or l23.get()=='':
         messagebox.showerror('Error','Fields cannot be empty')
    else:
        PhoneNumber=l23.get()
        if PhoneNumber.isdigit() and len(PhoneNumber) == 10:
            print("success")
        else:
            return
        EmployeeId =random_num()
        EmployeeName=l7.get()
        DateOfBirth=l10.get()
        Address=l12.get()
        Qualification=l14.get()
        Department=l16.get()
        Salary=str(l19.get())
        JoiningDate=l21.get()

        Photo=l30.get()
        connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
        c=connection.cursor()
        # insert_query ="INSERT INTO college1 ('PatientId','PatientName','DateOfBirth','Address','Diagnosis','NameOfTablet','NoOfTablet','Issuedate','ExpiryDate') VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        # vals=(PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate)
        # c.execute("insert into college1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PatientId,PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate))
        c.execute("insert into Employee4 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(EmployeeId,EmployeeName,DateOfBirth,Address,Qualification,Department,Salary,JoiningDate,PhoneNumber,Photo))
        connection.commit()
        # c.commit()
        # c.close()
        messagebox.showinfo('Success','Employee Registered Successfully')
        return


def documents():
    
    return



#_____________________________________appreances___________________________________________________________________
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


#______________________________________window for add patient______________________________________________________
qap=customtkinter.CTk()
qap.geometry("1520x700+0+0")
qap.title("Hospital")

l2=tkinter.Label(qap,bd=20,relief="ridge",text="+ QuantumCare Hospital +",fg="cyan",bg="darkblue",font=("times new roman",50,"bold"))
l2.pack(side="top",fill="x")

img2=customtkinter.CTkImage(dark_image=Image.open("emp.jpg"),light_image=Image.open("emp.jpg"),size=(1500,610))

l4=customtkinter.CTkLabel(master=qap,image=img2,width=1500,height=610,bg_color="cyan",text=None)   #(900,610),
l4.place(relx=0,rely=0.115)

l5=tkinter.Label(qap,bd=20,relief="ridge",fg="cyan",bg="#FBF8E6",font=("times new roman",50,"bold"),width=47,height=12)
l5.place(relx=0,rely=0.11)


# l5=customtkinter.CTkLabel(master=qap,image=img2,width=1500,height=610,bg_color="cyan",text=None)   #(900,610),
# l5.place(relx=0,rely=0.115)


#---------------------------------------------label ----------------------------------------------------------

#width=,height=,corner_radius=,bg_color="Transparent"
l3=customtkinter.CTkLabel(master=l5,text="Employee ID",font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent",corner_radius=6)#,text_color="white")
l3.place(x=40,y=45)

l6=customtkinter.CTkLabel(master=l5,text=str(random_num()),text_color="black",font=("times new roman",20,"bold"),fg_color="#e1dfcf",bg_color="#FBF8E6",corner_radius=15,width=400)
l6.place(x=345,y=45)

l9=customtkinter.CTkLabel(master=l5,text="Employee Name",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l9.place(x=40,y=105)

l7=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
l7.place(x=345,y=105)

l8=customtkinter.CTkLabel(master=l5,text="Date Of Birth",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l8.place(x=40,y=165)

l10=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15,width=400)#,bg_color="#192841",corner_radius=6,border_color="yellow",border_width=2)
l10.place(x=345,y=165)

l11=customtkinter.CTkLabel(master=l5,text="Address",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l11.place(x=40,y=225)

l12=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15,width=400)
l12.place(x=345,y=225)

l13=customtkinter.CTkLabel(master=l5,text="Qualification",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l13.place(x=40,y=285)

l14=customtkinter.CTkComboBox(master=l5,values=["MBBS","MD","BAMS","HSC","SSC","Medical Graduate","Bachelor of Naturopathy","BDS","BAMS"],width=400)
l14.place(x=345,y=285)

# lblNameTablet=tkinter.Label(l5,text="Names Of Tablets",font=("times new roman",12,"bold"),padx=2,pady=6)
# lblNameTablet.grid(row=0,column=0)

# comNameTablet=ttk.Combobox(l5,font=("times new roman",12,"bold"),
#                                                             width=70,height=80)Dopamine
# Outpatient department (OPD), Surgical department, Inpatient service (IP), Nursing department, Physical medicine, Paramedical department, and Rehabilitation department, Dietary department, Pharmacy department,
# comNameTablet["values"]=("Ativan","Cymbalta","Otezla","Viagra","Boldcare","Bangali@Baba")
# comNameTablet.place(x=525,y=500)

l16=customtkinter.CTkComboBox(master=l5,values=[" Outpatient department (OPD)","Surgical department"," Nursing department","Paramedical department","Pharmacy department","Non-professional services"],width=400)
l16.place(x=345,y=345)

l17=customtkinter.CTkLabel(master=l5,text="Department",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l17.place(x=40,y=345)

# l18=customtkinter.CTkSlider(master=l5,from_=3,to=30,number_of_steps=10)
# l18.place(x=345,y=405)

l18=customtkinter.CTkLabel(master=l5,text="Salary",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l18.place(x=40,y=405)


l19=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
l19.place(x=345,y=405)


l20=customtkinter.CTkLabel(master=l5,text="Joining Date",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l20.place(x=40,y=465)


l21=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
l21.place(x=345,y=465)


l22=customtkinter.CTkLabel(master=l5,text="Phone Number",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l22.place(x=40,y=525)


l23=customtkinter.CTkEntry(master=l5,font=("times new roman",20,"bold"),fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
l23.place(x=345,y=525)

l33=customtkinter.CTkLabel(master=l5,text="Photo :",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l33.place(x=900,y=200)

l30=customtkinter.CTkEntry(master=l5,placeholder_text="Enter Image Name...",font=("times new roman",20,"bold"),fg_color="white",width=300,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
l30.place(x=900,y=230)

l32=tkinter.Label(l5,bd=20,relief="ridge",fg="cyan",bg="light yellow",font=("times new roman",50,"bold"),width=7,height=3)
l32.place(x=1400,y=10)
#906be4
#00b6bc
#002f9b



# btn4=customtkinter.CTkButton(master=l5,text="Verify Image",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=photo)
# btn4.place(relx=0.78,rely=0.47)

btn4=customtkinter.CTkButton(master=l5,text="Upload",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=upload_document)
btn4.place(relx=0.72,rely=0.45)

btn5=customtkinter.CTkButton(master=l5,text="View Image",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=photo)
btn5.place(relx=0.85,rely=0.45)

# l36=customtkinter.CTkLabel(master=l5,text="Documents :",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
# l36.place(x=900,y=350)

# btn5=customtkinter.CTkButton(master=l5,text="Upload",text_color="white",corner_radius=6,border_color="orange",fg_color="blue",border_width=3,hover_color="dark green",command=documents)
# btn5.place(relx=0.78,rely=0.67)





btn2=customtkinter.CTkButton(master=l5,text="Go Back",corner_radius=6,border_color="RED",fg_color="transparent",border_width=3,hover_color="RED",command=back,text_color="Black")
btn2.place(relx=0.86,rely=0.9)

btn3=customtkinter.CTkButton(master=l5,text="Confirm",corner_radius=6,border_color="light green",fg_color="blue",border_width=3,hover_color="blue",command=insert)
btn3.place(relx=0.73,rely=0.9)



qap.mainloop()
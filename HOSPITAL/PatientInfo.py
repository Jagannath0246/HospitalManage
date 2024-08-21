import tkinter
# from tkinter import *
import customtkinter
import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from subprocess import call
import mysql.connector
# import mysql.connector as c
import random
# from customtkinter.windows import CTkComboBox
# from customtkinter.widgets import CTkComboBox




#use Table  Patient11
def insert():

    connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
    c=connection.cursor()
    #cursor.execute("SELECT DISTINCT column_name FROM your_table;") 
    # insert_query ="INSERT INTO college1 ('PatientId','PatientName','DateOfBirth','Address','Diagnosis','NameOfTablet','NoOfTablet','Issuedate','ExpiryDate') VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    # vals=(PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate)
    c.execute("SELECT PatientId FROM Patient11;")
    data = c.fetchall()
    
    value = [item[0] for item in data]
    connection.commit()
    # c.commit()
    # c.close()
    return value

"""
def search():
    connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
    c=connection.cursor()
    xy=int(l50.get())
    c.execute("SELECT PatientName FROM college1 WHERE PatientId = %s;", (xy,))
    PatientName1=c.fetchone()


    connection.commit()
    return PatientName1
"""

def fetch_patient_info(patient_id):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')

        # Create cursor object
        cursor = connection.cursor()

        # Execute query to fetch patient info
        cursor.execute("SELECT PatientName,Address,DateOfBirth,Diagnosis,FatherName,MotherName,BloodGroup,PhoneNumber,Prescription,Photo FROM Patient11 WHERE PatientId = %s;", (patient_id,))

        # Fetch patient info
        patient_info = cursor.fetchone()

        return patient_info

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        # Close cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_patient_info():
    # Get selected patient ID from combobox++
    selected_patient_id = l50.get()

    # Fetch patient info based on selected ID
    patient_info = fetch_patient_info(selected_patient_id)
    print(patient_info)
    if patient_info:
        # Update labels with patient info
        l7.configure(text=" " + patient_info[0])
        l12.configure(text=" " + patient_info[1])
        l10.configure(text=" " + str(patient_info[2]))
        l14.configure(text=" " + str(patient_info[3]))
        l24.configure(text=" " + str(patient_info[4]))
        l19.configure(text=" " + str(patient_info[5]))
        l21.configure(text=" " + str(patient_info[6]))
        l23.configure(text=" " + str(patient_info[7]))
        l26.configure(text=" " + str(patient_info[8]))
        filename = patient_info[9]
        img2 = customtkinter.CTkImage(dark_image=Image.open(filename), light_image=Image.open(filename), size=(215,205))
        l31 = customtkinter.CTkLabel(master=l32, image=img2, width=200, height=200, bg_color="cyan", text=None)
        l31.place(x=0, y=0)
        return

        
    else:
        messagebox.showerror('Error','Invalid Patient ID')



def back():

    sap.destroy()
    call(['python','main.py'])

#_____________________________________appreances___________________________________________________________________
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


#______________________________________window for add patient______________________________________________________
sap=customtkinter.CTk()
sap.geometry("1520x700+0+0")
sap.title("Hospital")

l2=tkinter.Label(sap,bd=20,relief="ridge",text="+ QuantumCare Hospital +",fg="cyan",bg="darkblue",font=("times new roman",50,"bold"))
l2.pack(side="top",fill="x")


# img2=customtkinter.CTkImage(dark_image=Image.open("aapp.jpg"),light_image=Image.open("aapp.jpg"),size=(1500,610))

# l4=customtkinter.CTkLabel(master=sap,image=img2,width=1500,height=610,bg_color="cyan",text=None)   #(900,610),
# l4.place(relx=0,rely=0.115)

l5=tkinter.Label(sap,bd=20,relief="ridge",fg="cyan",bg="#cfe2f3",font=("times new roman",50,"bold"),width=47,height=12)
l5.place(relx=0,rely=0.11)

l3=customtkinter.CTkLabel(master=l5,text="Patient ID",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l3.place(x=40,y=45)


l9=customtkinter.CTkLabel(master=l5,text="Patient Name",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l9.place(x=40,y=105)


l7=customtkinter.CTkLabel(master=l5,text=" ",text_color="black",font=("times new roman",20,"bold"),fg_color="white",bg_color="#cfe2f3",corner_radius=6,width=400)
l7.place(x=345,y=105)

l8=customtkinter.CTkLabel(master=l5,text="Date Of Birth",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l8.place(x=40,y=165)

l10=customtkinter.CTkLabel(master=l5,text=" ",text_color="black",font=("times new roman",20,"bold"),fg_color="white",bg_color="#cfe2f3",corner_radius=6,width=400)
l10.place(x=345,y=165)

l11=customtkinter.CTkLabel(master=l5,text="Address",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l11.place(x=40,y=225)

l12=customtkinter.CTkLabel(master=l5,text=" ",text_color="black",font=("times new roman",20,"bold"),fg_color="white",bg_color="#cfe2f3",corner_radius=6,width=400)
l12.place(x=345,y=225)

l13=customtkinter.CTkLabel(master=l5,text="Diagnosis",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l13.place(x=40,y=285)

l14=customtkinter.CTkLabel(master=l5,text=" ",text_color="black",font=("times new roman",20,"bold"),fg_color="white",bg_color="#cfe2f3",corner_radius=6,width=400)
l14.place(x=345,y=285)

l17=customtkinter.CTkLabel(master=l5,text="Father Name",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l17.place(x=40,y=345)

l24=customtkinter.CTkLabel(master=l5,text=" ",text_color="black",font=("times new roman",20,"bold"),fg_color="white",bg_color="#cfe2f3",corner_radius=6,width=400)
l24.place(x=345,y=345)

# l18=customtkinter.CTkSlider(master=l5,from_=3,to=30,number_of_steps=10)
# l18.place(x=345,y=405)

l18=customtkinter.CTkLabel(master=l5,text="Mother Name",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l18.place(x=40,y=405)


l19=customtkinter.CTkLabel(master=l5,text=" ",text_color="black",font=("times new roman",20,"bold"),fg_color="white",bg_color="#cfe2f3",corner_radius=6,width=400)
l19.place(x=345,y=405)


l20=customtkinter.CTkLabel(master=l5,text="Blood Group",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l20.place(x=40,y=465)


l21=customtkinter.CTkLabel(master=l5,text=" ",text_color="black",font=("times new roman",20,"bold"),fg_color="white",bg_color="#cfe2f3",corner_radius=6,width=400)
l21.place(x=345,y=465)

l22=customtkinter.CTkLabel(master=l5,text="Phone Number",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l22.place(x=40,y=525)


l23=customtkinter.CTkLabel(master=l5,text=" ",text_color="black",font=("times new roman",20,"bold"),fg_color="white",bg_color="#cfe2f3",corner_radius=6,width=400)
l23.place(x=345,y=525)

valux=insert()
valux1 = [str(value) for value in valux]

l50=customtkinter.CTkComboBox(master=l5,values=valux1,width=400)
l50.place(x=345,y=45)

'''
# def notneeded():
    Create Combobox to select patient ID
    combo_patient_id = ttk.Combobox(sap,width=90,height=50)
    combo_patient_id.place(x=550,y=215)
    combo_patient_id = ctk.CTkComboBox(sap,width=90)
    combo_patient_id.place(x=550,y=210)

    Fetch patient IDs from database and populate Combobox
    try:
        connection = mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
        cursor = connection.cursor()
        cursor.execute("SELECT PatientId FROM Patient2;")
        patient_ids = [patient_id[0] for patient_id in cursor.fetchall()]
        combo_patient_id['values'] = patient_ids
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    Create button to fetch patient info
    button_fetch_info = ttk.Button(sap, text="Fetch Info", command=get_patient_info)
    button_fetch_info.place()
'''


l27=customtkinter.CTkLabel(master=l5,text="Prescription :",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l27.place(x=900,y=270)

l26=customtkinter.CTkLabel(master=l5,text=" ",text_color="black",font=("times new roman",20,"bold"),fg_color="white",bg_color="#cfe2f3",corner_radius=6,width=300,height=200)
l26.place(x=900,y=300)


l32=tkinter.Label(sap,bd=20,relief="ridge",fg="cyan",bg="#906be4",font=("times new roman",50,"bold"),width=8,height=4)
l32.place(x=1400,y=170)
#906be4
#00b6bc
#002f9b

btn2=customtkinter.CTkButton(master=l5,text="Go Back",text_color="black",corner_radius=6,border_color="RED",fg_color="transparent",border_width=3,hover_color="RED",command=back)
btn2.place(relx=0.86,rely=0.9)

btn3=customtkinter.CTkButton(master=l5,text="Search",text_color="black",corner_radius=6,border_color="light green",fg_color="transparent",border_width=3,hover_color="light green",command=get_patient_info)
btn3.place(relx=0.73,rely=0.9)



# btn3=customtkinter.CTkButton(master=l5,text="Search",corner_radius=6,border_color="light green",fg_color="transparent",border_width=3,hover_color="blue",command=get_patient_info)
# btn3.place(relx=0.73,rely=0.9)

# btn2=customtkinter.CTkButton(master=l5,text="Go Back",corner_radius=6,border_color="RED",fg_color="transparent",border_width=3,hover_color="RED",command=back)
# btn2.place(relx=0.86,rely=0.9)
sap.mainloop()


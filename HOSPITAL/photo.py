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



def insert():

    connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
    c=connection.cursor()
    #cursor.execute("SELECT DISTINCT column_name FROM your_table;") 
    # insert_query ="INSERT INTO college1 ('PatientId','PatientName','DateOfBirth','Address','Diagnosis','NameOfTablet','NoOfTablet','Issuedate','ExpiryDate') VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    # vals=(PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate)
    c.execute("SELECT patid FROM pat;")
    data = c.fetchall()
    
    value = [item[0] for item in data]
    connection.commit()
    # c.commit()
    # c.close()
    return value


def fetch_patient_info(patient_id):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')

        # Create cursor object
        cursor = connection.cursor()

        # Execute query to fetch patient info
        cursor.execute("SELECT photo FROM pat WHERE patid = %s;", (patient_id,))

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
    return patient_info
    # if patient_info:
    #     # Update labels with patient info
    #     l7.configure(text=" " + patient_info[0])
    #     # l12.configure(text=" " + patient_info[1])
    #     # l10.configure(text=" " + str(patient_info[2]))
    #     # l14.configure(text=" " + str(patient_info[3]))
    #     # l24.configure(text=" " + str(patient_info[4]))
    #     # l19.configure(text=" " + str(patient_info[5]))
    #     # l21.configure(text=" " + str(patient_info[6]))
    #     # l23.configure(text=" " + str(patient_info[7]))
    #     # l26.configure(text=" " + str(patient_info[8]))
    #     return

        
    # else:
    #     messagebox.showerror('Error','Invalid Patient ID')

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


#______________________________________window for add patient______________________________________________________
sap=customtkinter.CTk()
sap.geometry("1520x700+0+0")
sap.title("Hospital")

l2=tkinter.Label(sap,bd=20,relief="ridge",text="+ Hospital Management System +",fg="cyan",bg="darkblue",font=("times new roman",50,"bold"))
l2.pack(side="top",fill="x")


img2=customtkinter.CTkImage(dark_image=Image.open("aapp.jpg"),light_image=Image.open("aapp.jpg"),size=(1500,610))

l4=customtkinter.CTkLabel(master=sap,image=img2,width=1500,height=610,bg_color="cyan",text=None)   #(900,610),
l4.place(relx=0,rely=0.115)

l5=tkinter.Label(sap,bd=20,relief="ridge",fg="cyan",bg="#cfe2f3",font=("times new roman",50,"bold"),width=47,height=12)
l5.place(relx=0,rely=0.11)


l3=customtkinter.CTkLabel(master=l5,text="Patient ID",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
l3.place(x=40,y=45)

valux=insert()
valux1 = [str(value) for value in valux]

l50=customtkinter.CTkComboBox(master=l5,values=valux1,width=400)
l50.place(x=345,y=45)

def photo():
    patient_info1 = get_patient_info()
    if patient_info1:
        # Extract the filename from the tuple
        filename = patient_info1[0]
        
        # Open the image using the filename
        img2 = customtkinter.CTkImage(dark_image=Image.open(filename), light_image=Image.open(filename), size=(500,610))

        l4 = customtkinter.CTkLabel(master=l5, image=img2, width=500, height=610, bg_color="cyan", text=None)
        l4.place(relx=0, rely=0.115)
    else:
        messagebox.showerror('Error', 'Failed to fetch patient information')

    return

# def photo():
#     patient_info1=str(get_patient_info())

#     img2=customtkinter.CTkImage(dark_image=Image.open(patient_info1),light_image=Image.open(patient_info1),size=(500,610))

#     l4=customtkinter.CTkLabel(master=l5,image=img2,width=500,height=610,bg_color="cyan",text=None)   #(900,610),
#     l4.place(relx=0,rely=0.115)
#     return


btn3=customtkinter.CTkButton(master=l5,text="Search",text_color="black",corner_radius=6,border_color="light green",fg_color="transparent",border_width=3,hover_color="light green",command=photo)
btn3.place(relx=0.73,rely=0.9)

sap.mainloop()
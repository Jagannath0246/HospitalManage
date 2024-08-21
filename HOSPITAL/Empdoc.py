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

def back1():
    oap.destroy()

# def back2():
#     ll51.destroy()
    
def insert():
    # PatientId=
    # PatientName=l7.get()
    # DateOfBirth=l10.get()
    # Address=l12.get()
    # Diagnosis=l14.get()
    # NameOfTablet=l16.get()
    # NoOfTablet=l19.get()
    # Issuedate=l21.get()
    # ExpiryDate=l23.get()

    connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
    c=connection.cursor()
    #cursor.execute("SELECT DISTINCT column_name FROM your_table;") 
    # insert_query ="INSERT INTO college1 ('PatientId','PatientName','DateOfBirth','Address','Diagnosis','NameOfTablet','NoOfTablet','Issuedate','ExpiryDate') VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    # vals=(PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate)
    c.execute("SELECT EmployeeId FROM Employee4;")
    data = c.fetchall()
    
    value = [item[0] for item in data]
    connection.commit()
    # c.commit()
    # c.close()
    return value


# def get_patient_info():
#     # Get selected patient ID from combobox++
#     selected_patient_id = l50.get()

#     # Fetch patient info based on selected ID
#     patient_info = fetch_patient_info(selected_patient_id)
#     print(patient_info)
#     if patient_info:
#         # Update labels with patient info
#         l7.configure(text=" " + patient_info[0])


#
def UploadToDatabase():
    # if ll7.get()=='' or ll10.get()=='' or ll12.get()=='' or ll14.get()=='' or ll16.get()=='' or ll19.get()=='' or ll21.get()=='':
    #      messagebox.showerror('Error','Fields cannot be empty')
    # else:
    #     EmployeeId =random_num()
    #     EmployeeName=ll7.get()
    #     DateOfBirth=ll10.get()
    #     Address=ll12.get()
    #     Qualification=ll14.get()
    #     Department=ll16.get()
    #     Salary=str(ll19.get())
    #     JoiningDate=ll21.get()
    #     connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
    #     c=connection.cursor()
    #     # insert_query ="INSERT INTO college1 ('PatientId','PatientName','DateOfBirth','Address','Diagnosis','NameOfTablet','NoOfTablet','Issuedate','ExpiryDate') VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    #     # vals=(PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate)
    #     # c.execute("insert into college1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PatientId,PatientName,DateOfBirth,Address,Diagnosis,NameOfTablet,NoOfTablet,Issuedate,ExpiryDate))
    #     c.execute("insert into Employee4 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(EmployeeId,EmployeeName,DateOfBirth,Address,Qualification,Department,Salary,JoiningDate))
    #     connection.commit()
    #     # c.commit()
    #     # c.close()
    #     messagebox.showinfo('Success','Welcome')
    #     return

    return


def insert1():
    root = customtkinter.CTk()
    root.title("Document Viewer")

# Create widgets
    label_instruction = customtkinter.CTkLabel(root, text="Select a document:")
    entry_document = customtkinter.CTkEntry(root)
    button_upload = customtkinter.CTkButton(root, text="Upload Document", command=upload_document)
    button_verify = customtkinter.CTkButton(root, text="Verify", command=view_document)

# Place widgets using grid layout
    label_instruction.grid(row=0, column=0, padx=10, pady=10)
    entry_document.grid(row=0, column=1, padx=10, pady=10)
    button_upload.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    button_verify.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
    root.mainloop()
    # global photo_img  # Access the global variable
    
    # pap = customtkinter.CTk()
    # pap.geometry("1520x700+0+0")
    # pap.title("View Documents")
    
    # ll21=tkinter.Label(pap,bd=20,relief="ridge",text="+ Hospital Management System +",fg="cyan",bg="#FBF8E6",font=("times new roman",50,"bold"))
    # ll21.pack(side="top",fill="x")
    # ll51=tkinter.Label(pap,bd=20,relief="ridge",fg="cyan",bg="#FBF8E6",font=("times new roman",50,"bold"),width=47,height=12)
    # ll51.pack(anchor='center', expand=True)

    # Pic=ll6.get()
    # img2 = customtkinter.CTkImage(dark_image=Image.open(Pic), light_image=Image.open(Pic), size=(188,155))
    # photo_img = ImageTk.PhotoImage(img2)  # Assign the PhotoImage object to the global variable
    
    # l31 = customtkinter.CTkLabel(master=ll51, image=photo_img, width=500, height=500, bg_color="cyan", text=None)
    # l31.pack(anchor='center', expand=True)

    # btn21=customtkinter.CTkButton(master=ll51,text="Go Back",corner_radius=6,border_color="RED",fg_color="transparent",border_width=3,hover_color="RED",command=ll51.destroy,text_color="Black")
    # btn21.place(relx=0.86,rely=0.9)
    # pap.mainloop()
    # return


def view_document():
    document_path = ll6.get()
    if document_path:
        # Open the image and convert it to PNG format
        with Image.open(document_path) as img:
            img_png = img.convert("RGB")
            img_png.save("converted_image.png", format="PNG")

        # Open a new window to display the image
        new_window = tk.Toplevel(oap)
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
        ll6.insert(0, filename)


def view_document1():
    document_path = ll7.get()
    if document_path:
        # Open the image and convert it to PNG format
        with Image.open(document_path) as img:
            img_png = img.convert("RGB")
            img_png.save("converted_image.png", format="PNG")

        # Open a new window to display the image
        new_window = tk.Toplevel(oap)
        new_window.title("View Document")
        new_window.geometry("1900x1400+0+0")

        # Load the converted image
        image = ImageTk.PhotoImage(file="converted_image.png")

        # Display the image in a label
        image_label = tk.Label(new_window, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack()

def upload_document1():
    filename = filedialog.askopenfilename(title="Select a document")
    if filename:
        # Display the filename in the entry widget
        ll7.insert(0, filename)

def view_document2():
    document_path = ll10.get()
    if document_path:
        # Open the image and convert it to PNG format
        with Image.open(document_path) as img:
            img_png = img.convert("RGB")
            img_png.save("converted_image.png", format="PNG")

        # Open a new window to display the image
        new_window = tk.Toplevel(oap)
        new_window.title("View Document")
        new_window.geometry("1900x1400+0+0")

        # Load the converted image
        image = ImageTk.PhotoImage(file="converted_image.png")

        # Display the image in a label
        image_label = tk.Label(new_window, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack()

def upload_document2():
    filename = filedialog.askopenfilename(title="Select a document")
    if filename:
        # Display the filename in the entry widget
        ll10.insert(0, filename)


def view_document4():
    document_path = ll14.get()
    if document_path:
        # Open the image and convert it to PNG format
        with Image.open(document_path) as img:
            img_png = img.convert("RGB")
            img_png.save("converted_image.png", format="PNG")

        # Open a new window to display the image
        new_window = tk.Toplevel(oap)
        new_window.title("View Document")
        new_window.geometry("1900x1400+0+0")

        # Load the converted image
        image = ImageTk.PhotoImage(file="converted_image.png")

        # Display the image in a label
        image_label = tk.Label(new_window, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack()

def upload_document4():
    filename = filedialog.askopenfilename(title="Select a document")
    if filename:
        # Display the filename in the entry widget
        ll14.insert(0, filename)


def view_document5():
    document_path = ll16.get()
    if document_path:
        # Open the image and convert it to PNG format
        with Image.open(document_path) as img:
            img_png = img.convert("RGB")
            img_png.save("converted_image.png", format="PNG")

        # Open a new window to display the image
        new_window = tk.Toplevel(oap)
        new_window.title("View Document")
        new_window.geometry("1900x1400+0+0")

        # Load the converted image
        image = ImageTk.PhotoImage(file="converted_image.png")

        # Display the image in a label
        image_label = tk.Label(new_window, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack()

def upload_document5():
    filename = filedialog.askopenfilename(title="Select a document")
    if filename:
        # Display the filename in the entry widget
        ll16.insert(0, filename)

def view_document6():
    document_path = ll19.get()
    if document_path:
        # Open the image and convert it to PNG format
        with Image.open(document_path) as img:
            img_png = img.convert("RGB")
            img_png.save("converted_image.png", format="PNG")

        # Open a new window to display the image
        new_window = tk.Toplevel(oap)
        new_window.title("View Document")
        new_window.geometry("1900x1400+0+0")

        # Load the converted image
        image = ImageTk.PhotoImage(file="converted_image.png")

        # Display the image in a label
        image_label = tk.Label(new_window, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack()

def upload_document6():
    filename = filedialog.askopenfilename(title="Select a document")
    if filename:
        # Display the filename in the entry widget
        ll19.insert(0, filename)

def view_document7():
    document_path = ll21.get()
    if document_path:
        # Open the image and convert it to PNG format
        with Image.open(document_path) as img:
            img_png = img.convert("RGB")
            img_png.save("converted_image.png", format="PNG")

        # Open a new window to display the image
        new_window = tk.Toplevel(oap)
        new_window.title("View Document")
        new_window.geometry("1900x1400+0+0")

        # Load the converted image
        image = ImageTk.PhotoImage(file="converted_image.png")

        # Display the image in a label
        image_label = tk.Label(new_window, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack()

def upload_document7():
    filename = filedialog.askopenfilename(title="Select a document")
    if filename:
        # Display the filename in the entry widget
        ll21.insert(0, filename)



def view_document3():
    document_path = ll12.get()
    if document_path:
        # Open the image and convert it to PNG format
        with Image.open(document_path) as img:
            img_png = img.convert("RGB")
            img_png.save("converted_image.png", format="PNG")

        # Open a new window to display the image
        new_window = tk.Toplevel(oap)
        new_window.title("View Document")
        new_window.geometry("1900x1400+0+0")

        # Load the converted image
        image = ImageTk.PhotoImage(file="converted_image.png")

        # Display the image in a label
        image_label = tk.Label(new_window, image=image)
        image_label.image = image  # Keep a reference to the image to prevent garbage collection
        image_label.pack()

def upload_document3():
    filename = filedialog.askopenfilename(title="Select a document")
    if filename:
        # Display the filename in the entry widget
        ll12.insert(0, filename)

# def insert1():
    
#     # ll51=tkinter.Label(oap,bd=20,relief="ridge",fg="cyan",bg="#FBF8E6",font=("times new roman",50,"bold"),width=47,height=12)
#     # ll51.pack(anchor='center', expand=True)
#     def back2():
#         ll51.destroy()
#         return
    
#     ll51=tkinter.Label(oap,bd=20,relief="ridge",fg="cyan",bg="#FBF8E6",font=("times new roman",50,"bold"),width=47,height=12)
#     ll51.pack(anchor='center', expand=True)

#     Pic=ll6.get()
#     img2 = customtkinter.CTkImage(dark_image=Image.open(Pic), light_image=Image.open(Pic), size=(188,155))
#     l31 = customtkinter.CTkLabel(master=ll51, image=img2, width=500, height=500, bg_color="cyan", text=None)
#     l31.pack(anchor='center', expand=True)


#     btn21=customtkinter.CTkButton(master=ll51,text="Go Back",corner_radius=6,border_color="RED",fg_color="blue",border_width=3,hover_color="RED",command=back2,text_color="Black")
#     btn21.place(relx=0.56,rely=0.5)
    
    
#     return



oap=customtkinter.CTk()
oap.geometry("1520x700+0+0")
oap.title("Employee Documents")
ll2=tkinter.Label(oap,bd=20,relief="ridge",text="+ Hospital Management System +",fg="cyan",bg="darkblue",font=("times new roman",50,"bold"))
ll2.pack(side="top",fill="x")
ll5=tkinter.Label(oap,bd=20,relief="ridge",fg="cyan",bg="#FBF8E6",font=("times new roman",50,"bold"),width=47,height=12)
ll5.place(relx=0,rely=0.11)

btn11=customtkinter.CTkButton(master=ll5,text="Confirm",corner_radius=6,border_color="light green",fg_color="blue",border_width=3,hover_color="blue",command=UploadToDatabase)
btn11.place(relx=0.73,rely=0.9)

btn12=customtkinter.CTkButton(master=ll5,text="Go Back",corner_radius=6,border_color="RED",fg_color="transparent",border_width=3,hover_color="RED",command=back1,text_color="Black")
btn12.place(relx=0.86,rely=0.9)

ll3=customtkinter.CTkLabel(master=ll5,text="SSC Certificate :",corner_radius=6,font=("times new roman",24,"bold"),text_color="black",fg_color="transparent",bg_color="#FBF8E6")
ll3.place(x=40,y=45)

ll6=customtkinter.CTkEntry(master=ll5,font=("times new roman",20,"bold"),placeholder_text="Enter Image Name...",fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)

# l6=customtkinter.CTkLabel(master=l5,text=str(random_num()),text_color="black",font=("times new roman",20,"bold"),fg_color="#e1dfcf",bg_color="#cfe2f3",corner_radius=6,width=400)
ll6.place(x=345,y=45)

# btn13=customtkinter.CTkButton(master=ll5,text="Verify",corner_radius=6,border_color="light green",fg_color="#306e15",hover_color="#bb8f07",border_width=3,command=insert1)
# btn13.place(x=845,y=45)
btn114=customtkinter.CTkButton(master=ll5,text="Upload",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=upload_document)
btn114.place(x=1045,y=45)

btn115=customtkinter.CTkButton(master=ll5,text="Verify",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=view_document)
btn115.place(x=845,y=45)


ll9=customtkinter.CTkLabel(master=ll5,text="HSC Certificate :",corner_radius=6,font=("times new roman",24,"bold"),text_color="black",fg_color="transparent",bg_color="transparent")
ll9.place(x=40,y=105)

ll7=customtkinter.CTkEntry(master=ll5,font=("times new roman",20,"bold"),placeholder_text="Enter Image Name...",fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
ll7.place(x=345,y=105)

btn155=customtkinter.CTkButton(master=ll5,text="Verify",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=view_document1)
btn155.place(x=845,y=105)

btn156=customtkinter.CTkButton(master=ll5,text="Upload",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=upload_document1)
btn156.place(x=1045,y=105)

ll8=customtkinter.CTkLabel(master=ll5,text="Medical Degree :",corner_radius=6,font=("times new roman",24,"bold"),text_color="black",fg_color="transparent",bg_color="transparent")
ll8.place(x=40,y=165)

ll10=customtkinter.CTkEntry(master=ll5,font=("times new roman",20,"bold"),placeholder_text="Enter Image Name...",fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
ll10.place(x=345,y=165)

#==================================================================================================================
btn157=customtkinter.CTkButton(master=ll5,text="Verify",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=view_document2)
btn157.place(x=845,y=165)

btn158=customtkinter.CTkButton(master=ll5,text="Upload",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=upload_document2)
btn158.place(x=1045,y=165)


# btn15=customtkinter.CTkButton(master=ll5,text="Verify",corner_radius=6,border_color="light green",fg_color="#306e15",hover_color="#bb8f07",border_width=3,command=insert1)
# btn15.place(x=845,y=165)

ll11=customtkinter.CTkLabel(master=ll5,text="Adhar Card",corner_radius=6,font=("times new roman",24,"bold"),text_color="black",fg_color="transparent",bg_color="transparent")
ll11.place(x=40,y=225)

ll12=customtkinter.CTkEntry(master=ll5,font=("times new roman",20,"bold"),placeholder_text="Enter Image Name...",fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
ll12.place(x=345,y=225)

# btn16=customtkinter.CTkButton(master=ll5,text="Verify",corner_radius=6,border_color="light green",fg_color="#306e15",hover_color="#bb8f07",border_width=3,command=insert1)
# btn16.place(x=845,y=225)

btn159=customtkinter.CTkButton(master=ll5,text="Verify",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=view_document3)
btn159.place(x=845,y=225)

btn160=customtkinter.CTkButton(master=ll5,text="Upload",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=upload_document3)
btn160.place(x=1045,y=225)

ll13=customtkinter.CTkLabel(master=ll5,text="PAN Card",corner_radius=6,font=("times new roman",24,"bold"),text_color="black",fg_color="transparent",bg_color="transparent")
ll13.place(x=40,y=285)

# btn17=customtkinter.CTkButton(master=ll5,text="Verify",corner_radius=6,border_color="light green",fg_color="#306e15",hover_color="#bb8f07",border_width=3,command=insert1)
# btn17.place(x=845,y=285)

ll14=customtkinter.CTkEntry(master=ll5,font=("times new roman",20,"bold"),placeholder_text="Enter Image Name...",fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
ll14.place(x=345,y=285)

btn161=customtkinter.CTkButton(master=ll5,text="Verify",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=view_document4)
btn161.place(x=845,y=285)

btn162=customtkinter.CTkButton(master=ll5,text="Upload",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=upload_document4)
btn162.place(x=1045,y=285)
# btn11=customtkinter.CTkButton(master=l5,text="Confirm",corner_radius=6,border_color="light green",fg_color="blue",border_width=3,hover_color="blue",command=insert1)
# btn11.place(relx=0.73,rely=0.9)

# lblNameTablet=tkinter.Label(l5,text="Names Of Tablets",font=("times new roman",12,"bold"),padx=2,pady=6)
# lblNameTablet.grid(row=0,column=0)

# comNameTablet=ttk.Combobox(l5,font=("times new roman",12,"bold"),
#                                                             width=70,height=80)Dopamine
# Doxazosin
# Doxepin
# Doxorubicin
# comNameTablet.place(x=525,y=500)

# =customtkinter.CTkComboBox(master=l5,values=["Ativan","Cymbalta","Otezla","Dopamine","Doxazosin","Doxepin","Doxorubicin"],width=400)

ll16=customtkinter.CTkEntry(master=ll5,font=("times new roman",20,"bold"),placeholder_text="Enter Image Name...",fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
ll16.place(x=345,y=345)

ll17=customtkinter.CTkLabel(master=ll5,text="Election Card",corner_radius=6,font=("times new roman",24,"bold"),text_color="black",fg_color="transparent",bg_color="transparent")
ll17.place(x=40,y=345)

# btn18=customtkinter.CTkButton(master=ll5,text="Verify",corner_radius=6,border_color="light green",fg_color="#306e15",hover_color="#bb8f07",border_width=3,command=insert1)
# btn18.place(x=845,y=345)

btn163=customtkinter.CTkButton(master=ll5,text="Verify",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=view_document5)
btn163.place(x=845,y=345)

btn164=customtkinter.CTkButton(master=ll5,text="Upload",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=upload_document5)
btn164.place(x=1045,y=345)

# l18=customtkinter.CTkSlider(master=l5,from_=3,to=30,number_of_steps=10)
# l18.place(x=345,y=405)

ll18=customtkinter.CTkLabel(master=ll5,text="Domicile Certificate :",corner_radius=6,font=("times new roman",24,"bold"),text_color="black",fg_color="transparent",bg_color="transparent")
ll18.place(x=40,y=405)


ll19=customtkinter.CTkEntry(master=ll5,font=("times new roman",20,"bold"),placeholder_text="Enter Image Name...",fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
ll19.place(x=345,y=405)

# btn19=customtkinter.CTkButton(master=ll5,text="Verify",corner_radius=6,border_color="light green",fg_color="#306e15",hover_color="#bb8f07",border_width=3,command=insert1)
# btn19.place(x=845,y=405)
btn165=customtkinter.CTkButton(master=ll5,text="Verify",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=view_document6)
btn165.place(x=845,y=405)

btn166=customtkinter.CTkButton(master=ll5,text="Upload",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=upload_document6)
btn166.place(x=1045,y=405)


ll20=customtkinter.CTkLabel(master=ll5,text="Undertaking Form :",corner_radius=6,font=("times new roman",24,"bold"),text_color="black",fg_color="transparent",bg_color="transparent")
ll20.place(x=40,y=465)


ll21=customtkinter.CTkEntry(master=ll5,font=("times new roman",20,"bold"),placeholder_text="Enter Image Name...",fg_color="white",width=400,bg_color="#FBF8E6",border_color="black",border_width=4,corner_radius=15)
ll21.place(x=345,y=465)

btn167=customtkinter.CTkButton(master=ll5,text="Verify",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=view_document7)
btn167.place(x=845,y=465)

btn168=customtkinter.CTkButton(master=ll5,text="Upload",text_color="white",corner_radius=6,border_color="red",fg_color="blue",border_width=3,hover_color="blue",command=upload_document7)
btn168.place(x=1045,y=465)

# btn110=customtkinter.CTkButton(master=ll5,text="Verify",corner_radius=6,border_color="light green",fg_color="#306e15",hover_color="#bb8f07",border_width=3,command=insert1)
# btn110

valux=insert()
valux1 = [str(value) for value in valux]

l50=customtkinter.CTkComboBox(master=ll5,values=valux1,width=400)
l50.place(x=345,y=10)




# l22=customtkinter.CTkLabel(master=l5,text="Phone Number",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
# l22.place(x=40,y=525)



# l23.place(x=345,y=525)


# l26=customtkinter.CTkLabel(master=l5,text="Prescription :",corner_radius=6,font=("times new roman",24,"bold"),fg_color="transparent",bg_color="transparent")
# l26.place(x=900,y=320)

# l25=CTkTextbox(l5,font=("times new roman",12,"bold"),width=300,height=180,border_width=2,border_color="black",scrollbar_button_color="grey")#,padx=2,pady=6)
# l25.place(x=900,y=350)










oap.mainloop()

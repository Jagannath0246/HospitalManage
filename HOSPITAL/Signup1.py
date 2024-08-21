import customtkinter
import tkinter
import messagebox

from tkinter import *


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
def signup3():
    if entry1.get() == '':
        messagebox.showerror('error', "please enter username")
        return

signup = customtkinter.CTk()
signup.geometry("700x600")
signup.title("signup page")

frame = customtkinter.CTkFrame(master=signup,width=400,height=500)
frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
l1=customtkinter.CTkLabel(master=frame,text="Fill the required details below",font=('century Gothic',20,'bold','underline'))
l1.place(x=50,y=30)
########################################################################################################################
l2 = customtkinter.CTkLabel(master=frame,text="Enter Your Username",font=('century Gothic', 15))
l2.place(x=70, y=100)

entry1=customtkinter.CTkEntry(master=frame,width=220,placeholder_text="As per your Library-Id")
entry1.place(x=70,y=130)

#######################################################################################################################

l3 = customtkinter.CTkLabel(master=frame,text="Enter your Registration No.",font=('century Gothic',15))
l3.place(x=70, y=180)

entry2= customtkinter.CTkEntry(master=frame,width=220, placeholder_text="RegNo.")
entry2.place(x=70,y=210)


#######################################################################################################################

l3 = customtkinter.CTkLabel(master=frame,text="Enter your Registration No.",font=('century Gothic',15))
l3.place(x=70, y=180)

entry2= customtkinter.CTkEntry(master=frame,width=220, placeholder_text="RegNo.")
entry2.place(x=70,y=210)

#######################################################################################################################

l4=customtkinter.CTkLabel(master=frame, text="Enter Your Password", font=('century Gothic', 15))
l4.place(x=70, y=260)

entry3=customtkinter.CTkEntry(master=frame,width=220, placeholder_text="Password", show="*")
entry3.place(x=70, y=290)


#######################################################################################################################




b1=customtkinter.CTkButton(master=frame, text="SignUp", width=220, height=40,command=signup3)
b1.place(x=70, y=400)


#######################################################################################################################


signup.mainloop()
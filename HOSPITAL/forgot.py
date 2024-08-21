import tkinter
# from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox




def aqw():
    forgot.destroy()

    import login

def verify():
    if box3.get()=='' or box4.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif box3.get()=='red' and box4.get()=='apple':
        messagebox.showinfo('Success','Your password is : 12345')
    elif box3.get()!='red' or box4.get()!='apple':
        messagebox.showerror('Error','Incorrect values')
# v=customtkinter.CTk()
# v.geometry("600x440+500+200")
# v.title("HINT")
# l1=customtkinter.CTkLabel(master=v,text="Your password is :",font=('Botthanie',20))
# l1.place(relx=0.25,rely=0.65)
# # l1=customtkinter.CTkLabel(master=v,text="Your password is :",font=('Botthanie',20))
# # l1.place(relx=0.25,rely=0.65)
# btn2=customtkinter.CTkButton(master=v,text="Go Back",corner_radius=6,border_color="RED",fg_color="transparent",border_width=3,hover_color="RED",command=v.destroy)
# btn2.place(relx=0.53,rely=0.85)
# v.mainloop()

forgot=customtkinter.CTk()
forgot.geometry("600x440+500+200")
forgot.title("Message Box")
#--------------------------------------------entry fielde for verifications-------------------------------------------------------------
l1=customtkinter.CTkLabel(master=forgot,text="Message Box")
l1.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
Frame1=customtkinter.CTkFrame(master=forgot,width=330,height=370,corner_radius=15,border_width=5,border_color="cyan")
Frame1.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)
l1=customtkinter.CTkLabel(master=Frame1,text="What is your Fav Colour ?",font=('Century Gothic',16))
l1.place(relx=0.25,rely=0.2)
box3=customtkinter.CTkEntry(master=Frame1,placeholder_text="answer....",border_color="cyan")
box3.place(relx=0.25,rely=0.27)
l2=customtkinter.CTkLabel(master=Frame1,text="What is your Fav Food?",font=('Century Gothic',16))
l2.place(relx=0.25,rely=0.35)
box4=customtkinter.CTkEntry(master=Frame1,placeholder_text="answer....",border_color="cyan")
box4.place(relx=0.25,rely=0.42)
btn1=customtkinter.CTkButton(master=Frame1,text="Verify",corner_radius=6,border_color="lightgreen",fg_color="transparent",border_width=3,hover_color="lightgreen",command=verify)
btn1.place(relx=0.34,rely=0.53)
btn2=customtkinter.CTkButton(master=Frame1,text="Go Back",corner_radius=6,border_color="RED",fg_color="transparent",border_width=3,hover_color="RED",command=aqw)
btn2.place(relx=0.53,rely=0.85)

forgot.mainloop()
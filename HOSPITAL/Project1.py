import customtkinter
import tkinter
import tkinter as Tk
import ctypes
from PIL import Image
from subprocess import call

def back():

    first.destroy()
    call(['python','main.py'])


customtkinter.set_appearance_mode("light")
first = customtkinter.CTk()
first.geometry("1520x700+0+0")

first.title('firstpage')


def Bill2():
    call(['python','Bill2.py'])

def bill():
    call(['python','bill.py'])

def categories():
    call(['python','category.py'])

def medicines():
    call(['python','Medicines.py'])


frame1=customtkinter.CTkFrame(master=first,width=1000,height=100)
frame1.place(x=320,y=10)

my_label2=customtkinter.CTkLabel(master=frame1,text='Welcome To The Medical',font=('century gothic',50,'bold'))
my_label2.place(x=170, y=10)


# screen_width = ctypes.windll.user32.GetSystemMetrics(0)
# screen_height = ctypes.windll.user32.GetSystemMetrics(1)
frame2=customtkinter.CTkFrame(master=first,width=250,height =600)
frame2.place(x=10,y=150)

btn_categories = customtkinter.CTkButton(master=frame2,text="Prescriptions",width=220,height=40,command=categories)
btn_categories.place(x=15, y=50)

btn_medicines = customtkinter.CTkButton(master=frame2,text="Medicines",width=220,height=40,command=medicines)
btn_medicines.place(y=150, x=15)


btn_doctors = customtkinter.CTkButton(master=frame2,text="Back",width=220,height=40,command=back)
btn_doctors.place(y=450, x=15)

btn_labtest = customtkinter.CTkButton(master=frame2,text="Search",width=220,height=40,command=bill)
btn_labtest.place(y=350, x=15)

btn_offers = customtkinter.CTkButton(master=frame2,text="Bill",width=220,height=40,command=Bill2)
btn_offers.place(y=250, x=15)

# w = (screen_width - screen_width) // 2
# h= (screen_height - screen_height) // 2

#my_image=customtkinter.CTkImage(light_image=Image.open('images/IMAGE.jpeg'),dark_image=Image.open('images/Image.jpeg'),size=(1500,750))

#my_label=customtkinter.CTkLabel(first,text="",image=my_image)
#my_label.pack(pady=10)


##dashboard=customtkinter.CTk()
# dashboard.geometry(f"{screen_width}x{screen_height}+{w}+{h}")
# dashboard.update_idletasks()
# dashboard.title("Dashboard")
#
# dashboard.mainloop()


frame3=customtkinter.CTkFrame(master=first,width=1200,height=600)
frame3.place(x=300,y=150)

my_image=customtkinter.CTkImage(light_image=Image.open('images/IMAGE.jpeg'),dark_image=Image.open('images/Image.jpeg'),size=(1200,600))

my_label=customtkinter.CTkLabel(frame3,text="",image=my_image)
my_label.pack()




first.mainloop()
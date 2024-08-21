
import customtkinter
import tkinter as tk
from tkinter import ttk
import tkinter
import pymysql
from subprocess import call
from tkinter import messagebox
import ctypes
from PIL import ImageTk, Image
from PIL import Image


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

screen_width = ctypes.windll.user32.GetSystemMetrics(0)
screen_height = ctypes.windll.user32.GetSystemMetrics(1)

w = (screen_width - screen_width) // 2
h= (screen_height - screen_height) // 2



root=customtkinter.CTk()
root.title("Users Dashboard")
root.geometry(f"{screen_width}x{screen_height}+{w}+{h}")
root.update_idletasks()



frame1 = tk.Frame(root,width=screen_width+350,height=screen_height+85)
frame1.configure(bg='lavender')
frame1.configure(highlightbackground="darkblue",highlightthickness=5)
frame1.pack()
l1=customtkinter.CTkLabel(master=frame1,text="Search The Medicines You Want",font=('century Gothic',35,'bold','underline'))
l1.place(x=220,y=0)


entry=customtkinter.CTkEntry(master=frame1,font=('century Gothic',20),width=400,placeholder_text="search")
entry.place(x=150,y=105)




tree = ttk.Treeview(root)
tree.configure(height=22)
tree['show'] = 'headings'


s = ttk.Style(root)
s.theme_use("clam")
s.configure(".", font=('arial', 12))
s.configure("Treeview.Heading", foreground='black', font=('arial', 15, 'bold'))

tree["columns"] = ("Serial_no", "Name", "Quantity","Location","Cost")
tree.column("Serial_no", width=280,minwidth=100, anchor=tk.CENTER)
tree.column("Name", width=280, minwidth=100, anchor=tk.CENTER)
tree.column("Quantity", width=280, minwidth=100, anchor=tk.CENTER)
tree.column("Location", width=280, minwidth=100, anchor=tk.CENTER)
tree.column("Cost", width=280, minwidth=100, anchor=tk.CENTER)



tree.heading("Serial_no", text="Serial No.", anchor=tk.CENTER)
tree.heading("Name", text="Medicine", anchor=tk.CENTER)
tree.heading("Quantity", text="Quantity", anchor=tk.CENTER)
tree.heading("Location", text="Location", anchor=tk.CENTER)
tree.heading("Cost", text="Cost", anchor=tk.CENTER)


tree.place(x=290,y=240)


def search():
    try:
        name = entry.get()
        print(name)
        conn = pymysql.connect(host='localhost', user='root', password='jms0246')
        my_cursor = conn.cursor()
        query1 = "use HospitalManagement"
        my_cursor.execute(query1)
        my_cursor.execute("SELECT * FROM Medicines2 WHERE name LIKE '%"+name+"%'")
        i = 0
        for ro in my_cursor:
            tree.insert('', i, text="", values=(ro[0], ro[1], ro[2],ro[3],ro[4]))
            i = i + 1
        conn.commit()
        conn.close()


    except:
        messagebox.showinfo('error',"No Such Book found")

def book():
    print("a")
   ###book cha definition

def back():
    root.destroy()



search=customtkinter.CTkButton(master=frame1,text="Search",font=(('century Gothic', 15,'bold')),command=search)
search.place(x=600,y=105)

book=customtkinter.CTkButton(master=frame1,text="Back",font=(('century Gothic', 15,'bold')),command=back)
book.place(x=800,y=105)

# book=customtkinter.CTkButton(master=frame1,text="Back",font=(('century Gothic', 15,'bold')),command=back)
# book.place(x=1000,y=105)






root.mainloop()
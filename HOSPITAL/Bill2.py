import customtkinter
import pymysql
from tkinter import messagebox
from PIL import ImageTk, Image

root=customtkinter.CTk()
root.geometry("1520x700+0+0")
root.config(bg="Grey")

def clear():
    e1.delete(0,"end")
    e2.delete(0,'end')
    # my_label2.destroy()
    # my_label3.destroy()
    # my_label4.destroy()
    # my_label5.destroy()


def search():
    if e1.get()=='' or e2.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    else:
        name=e1.get()
        quantity=e2.get()

        conn = pymysql.connect(host='localhost', user='root', password='jms0246')
        my_cursor = conn.cursor()
        query1 = "use HospitalManagement"
        my_cursor.execute(query1)
        query=("SELECT cost FROM Medicines2 WHERE name=%s")
        my_cursor.execute(query, (name,))
        result=my_cursor.fetchone()
        source_column_value = float(result[0])
        entry_value = float(e2.get())
        cost = abs(source_column_value * entry_value)


        #messagebox.showinfo("Cost", f"The calculated cost is: {cost}")

        my_label8 = customtkinter.CTkLabel(master=root, text='Name', font=('century gothic', 40, 'bold'))
        my_label8.place(x=500, y=300)

        my_label3 = customtkinter.CTkLabel(master=root, text=name, font=('century gothic', 40, 'bold'))
        my_label3.place(x=650, y=300)

        my_label4 = customtkinter.CTkLabel(master=root, text='Quantity', font=('century gothic', 40, 'bold'))
        my_label4.place(x=900, y=300)

        my_label5 = customtkinter.CTkLabel(master=root, text=quantity, font=('century gothic', 40, 'bold'))
        my_label5.place(x=1200, y=300)

        my_label6 = customtkinter.CTkLabel(master=root, text='Cost', font=('century gothic', 60, 'bold'))
        my_label6.place(x=500, y=500)

        my_label7 = customtkinter.CTkLabel(master=root, text= cost , font=('century gothic', 60, 'bold'))
        my_label7.place(x=800, y=500)

        conn.commit()
        conn.close()

img2=customtkinter.CTkImage(dark_image=Image.open("bag.jpg"),light_image=Image.open("bag.jpg"),size=(1500,700))

l4=customtkinter.CTkLabel(master=root,image=img2,width=1500,height=700,bg_color="cyan",text=None)   #(900,610),
l4.place(relx=0,rely=0)

frame1=customtkinter.CTkFrame(master=root,width=700,height=100,fg_color="blue")
frame1.place(x=400,y=10)

frame2=customtkinter.CTkFrame(master=root,width=700,height=100,fg_color="blue")
frame2.place(x=400,y=10)


#e1=customtkinter.CTkEntry(master=frame2,width=200,height=40,placeholder_text="Search Medicine",font=('century gothic',20))
#e1.place(x=15, y=300)

my_label2=customtkinter.CTkLabel(master=frame2,text='RECEIPT',font=('century gothic',60,'bold'),text_color="white")
my_label2.place(x=200, y=10)
# my_label10=customtkinter.CTkLabel(master=frame1,text='RECEIPT',text_color="White")
# my_label10.place(x=200,y=10)

frame2=customtkinter.CTkFrame(master=root,width=250,height =400,border_color="cyan",border_width=5)
frame2.place(x=10,y=150)

e1=customtkinter.CTkEntry(master=frame2,width=200,height=40,placeholder_text="name",font=('century gothic',20))
e1.place(x=15, y=100)

e2=customtkinter.CTkEntry(master=root,width=200,height=40,placeholder_text="quantity",font=('century gothic',20))
e2.place(x=25, y=300)


btn_doctors = customtkinter.CTkButton(master=frame2,text="Search",width=220,height=40,command=search)
btn_doctors.place(y=250, x=15)

#btn_doctors = customtkinter.CTkButton(master=frame2,text="Add to cart",width=220,height=40)
#btn_doctors.place(y=250, x=15)

btn_doctors = customtkinter.CTkButton(master=frame2,text="Clear",width=220,height=40,command=clear)
btn_doctors.place(y=300, x=15)



#btn_addtocart = customtkinter.CTkButton(master=frame2,text="Categories",width=220,height=40,)
#btn_addtocart.place(x=15, y=50)
















root.mainloop()
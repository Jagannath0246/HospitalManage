import tkinter as tk
from tkinter import messagebox
import mysql.connector
import customtkinter as ctk

def search_prescription():
    patient_name = entry_patient_name.get()
    if not patient_name:
        messagebox.showwarning("Warning", "Please enter the patient's name.")
        return

    try:
        # Execute SQL query
        with mysql.connector.connect(
            host="localhost",
            user="root",
            password="jms0246",
            database="HospitalManagement"
        ) as db:
            cursor = db.cursor()
            cursor.execute("SELECT Prescription FROM Patient10 WHERE PatientName = %s", (patient_name,))
            result = cursor.fetchone()

            if result:
                # Show prescription in a new window
                prescription_window = tk.Toplevel(root)
                prescription_window.title("Prescription")

                prescription_label = ctk.CTkLabel(prescription_window, text=result[0])
                prescription_label.place(x=100,y=100)
            else:
                messagebox.showerror("Error", "Patient not found!")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error accessing database: {e}")

def back():
    root.destroy()

root = ctk.CTk()
root.geometry("400x500")

entry_patient_name = ctk.CTkEntry(master=root, width=50, placeholder_text="Search Patient", font=('century gothic', 14))
entry_patient_name.place(x=50, y=100)

frame_title = ctk.CTkFrame(master=root, width=700, height=100)
frame_title.place(x=50, y=10)

label_title = ctk.CTkLabel(master=frame_title, text='Prescription', font=('century gothic', 30, 'bold'))
label_title.place(x=200, y=10)

button_search = ctk.CTkButton(master=root, text="Search", width=10, height=2, command=search_prescription)
button_search.place(x=50, y=200)

button_back = ctk.CTkButton(master=root, text="Back", width=10, height=2, command=back)
button_back.place(x=150, y=200)

root.mainloop()
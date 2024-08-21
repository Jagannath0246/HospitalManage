import tkinter as tk
from tkinter import messagebox
from customtkinter import CTk
from customtkinter import DateEntry, TimeEntry

def get_birthdate():
    birthdate = f"{date_entry.get()} {time_entry.get()}"
    messagebox.showinfo("Birthdate", f"The selected birthdate is: {birthdate}")

# Create main window
root = CTk()
root.geometry("400x300")
root.title("Employee Birthdate Picker")

# Create DateEntry widget
date_entry = DateEntry(root, font=("Arial", 12))
date_entry.pack(pady=10)

# Create TimeEntry widget
time_entry = TimeEntry(root, font=("Arial", 12))
time_entry.pack(pady=10)

# Button to get the selected birthdate
get_birthdate_button = tk.Button(root, text="Get Birthdate", command=get_birthdate)
get_birthdate_button.pack(pady=10)

root.mainloop()
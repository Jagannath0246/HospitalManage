import tkinter as tk
from tkinter import ttk
import mysql.connector

def fetch_employee_info(emp_id):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')

        # Create cursor object
        cursor = connection.cursor()

        # Execute query to fetch employee info
        cursor.execute("SELECT PatientName FROM college1 WHERE PatientId = %s;", (PatientId,))

        # Fetch employee info
        employee_info = cursor.fetchone()

        return employee_info

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        # Close cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_employee_info():
    # Get selected employee ID from combobox
    selected_emp_id = combo_PatientID.get()

    # Fetch employee info based on selected ID
    employee_info = fetch_employee_info(selected_emp_id)

    if employee_info:
        # Update labels with employee info
        label_emp_name.config(text="Employee Name: " + employee_info[0])
        label_emp_address.config(text="Employee Address: " + employee_info[1])
    else:
        # Clear labels if employee info not found
        label_emp_name.config(text="Employee Name: ")
        label_emp_address.config(text="Employee Address: ")

# Create Tkinter window
root = tk.Tk()
root.title("Employee Information")

# Create Combobox to select employee ID
combo_PatientID = ttk.Combobox(root)
combo_PatientID.pack()

# Fetch employee IDs from database and populate Combobox
try:
    connection = mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
    cursor = connection.cursor()
    cursor.execute("SELECT PatientId FROM college1;")
    PatientId = [PatientID[0] for PatientID in cursor.fetchall()]
    combo_PatientID['values'] = PatientId
except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

# Create button to fetch employee info
button_fetch_info = ttk.Button(root, text="Fetch Info", command=get_employee_info)
button_fetch_info.pack()

# Create labels to display employee info
label_emp_name = ttk.Label(root, text="Employee Name: ")
label_emp_name.pack()
label_emp_address = ttk.Label(root, text="Employee Address: ")
label_emp_address.pack()

# Run Tkinter event loop
root.mainloop()
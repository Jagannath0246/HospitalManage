import tkinter as tk
from tkinter import ttk
import mysql.connector

def fetch_patient_info(patient_id):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')

        # Create cursor object
        cursor = connection.cursor()

        # Execute query to fetch patient info
        cursor.execute("SELECT PatientName,Address FROM college1 WHERE PatientId = %s;", (patient_id,))

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
    # Get selected patient ID from combobox
    selected_patient_id = combo_patient_id.get()

    # Fetch patient info based on selected ID
    patient_info = fetch_patient_info(selected_patient_id)

    if patient_info:
        # Update labels with patient info
        label_patient_name.config(text="Patient Name: " + patient_info[0])
        label_patient_address.config(text="Patient Address: " + patient_info[1])
    else:
        # Clear labels if patient info not found
        label_patient_name.config(text="Patient Name: ")
        label_patient_address.config(text="Patient Address: ")

# Create Tkinter window
root = tk.Tk()
root.title("Patient Information")

# Create Combobox to select patient ID
combo_patient_id = ttk.Combobox(root)
combo_patient_id.pack()

# Fetch patient IDs from database and populate Combobox
try:
    connection = mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
    cursor = connection.cursor()
    cursor.execute("SELECT PatientId FROM college1;")
    patient_ids = [patient_id[0] for patient_id in cursor.fetchall()]
    combo_patient_id['values'] = patient_ids
except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

# Create button to fetch patient info
button_fetch_info = ttk.Button(root, text="Fetch Info", command=get_patient_info)
button_fetch_info.pack()

# Create labels to display patient info
label_patient_name = ttk.Label(root, text="Patient Name: ")
label_patient_name.pack()
label_patient_address = ttk.Label(root, text="Patient Address: ")
label_patient_address.pack()

# Run Tkinter event loop
root.mainloop()
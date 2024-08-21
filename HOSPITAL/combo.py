import tkinter as tk
# import tkinter as tk
from tkinter import ttk
# from customtkinter.windows import CTkComboBox
import mysql.connector
# import mysql.connector as c
import random


# Function to fetch data from the database
def fetch_data():
    # Connect to your database (replace 'example.db' with your database file)
    connection=mysql.connector.connect(host='localhost',user='root',password='jms0246',port='3306',database='HospitalManagement')
    c=connection.cursor()

    # Create a cursor object to execute SQL queries
    

    # Execute the SQL query to fetch the values
    c.execute("SELECT DISTINCT PatientId FROM college1;") 
    # Replace 'your_table' with your table name and 'column_name' with the column you want to display in the dropdown

    # Fetch the result
    data = c.fetchall()

    # Close the cursor and connection
    
    connection.commit()

    # Extract values from the fetched data
    values = [item[0] for item in data]

    # Return the fetched values
    return values

# Create Tkinter window
root = tk.Tk()
root.title("Dropdown Box Example")

# Fetch data from the database
values = fetch_data()

# Create a CTkComboBox (dropdown box)
combo = ttk.Combobox(root, values=values, width=30)
combo.pack()


# Run the Tkinter event loop
root.mainloop()
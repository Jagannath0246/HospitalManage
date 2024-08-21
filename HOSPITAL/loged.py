import mysql.connector
from customtkinter.windows import CTkWindow, CTkLabel, CTkEntry, CTkButton

# Function to validate the login credentials
def validate_login(username, password):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        cursor = connection.cursor()

        # Query to check if the username and password match
        query = "SELECT * FROM Users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        # Close the database connection
        cursor.close()
        connection.close()

        return result is not None
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return False

# Function to handle login button click event
def login_clicked():
    username = entry_username.get()
    password = entry_password.get()
    if validate_login(username, password):
        # Login successful, display message
        label_status.config(text="Login successful", fg="green")
    else:
        # Login failed, display error message
        label_status.config(text="Invalid username or password", fg="red")

# Create the login window
window = CTkWindow(title="Login Page")

# Add username label and entry
label_username = CTkLabel(master=window, text="Username:")
label_username.pack()
entry_username = CTkEntry(master=window)
entry_username.pack()

# Add password label and entry
label_password = CTkLabel(master=window, text="Password:")
label_password.pack()
entry_password = CTkEntry(master=window, show="*")
entry_password.pack()

# Add login button
button_login = CTkButton(master=window, text="Login", command=login_clicked)
button_login.pack()

# Add label to display login status
label_status = CTkLabel(master=window, text="")
label_status.pack()

# Run the main loop
window.mainloop()
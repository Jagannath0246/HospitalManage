# from PIL import Image, ImageFont,ImageDraw,ImageTk
# import tkinter as tk

# root = tk.Tk()

# # Open the image
# image = Image.open("C:/Users/jagan/Desktop/HOSPITAL/emp.jpg")

# # Create a Tkinter-compatible image object
# photo = ImageTk.PhotoImage(image)

# # Get the width and height of the image
# width, height = image.size

# # Create a canvas with the same size as the image
# canvas = tk.Canvas(root, width=width, height=height)

# # Place the image on the canvas
# canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# # Add a label on the canvas
# label_text = "Transparent Label"
# label = tk.Label(canvas, text=label_text, bg="white", fg="black")  # Customize as needed
# label_window = canvas.create_window(50, 50, anchor=tk.NW, window=label)

# draw=ImageDraw.Draw(image)
# font1=ImageFont.truetype("arial.ttf",100)
# points=100,80
# string="Employee"
# color="Black"

# draw.text(points,string,color,font=font1)
# image.show()
# # Pack the canvas
# canvas.pack()

# root.mainloop()


import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Employee ID")

# Load the image
image = Image.open(r"C:/Users/jagan/Desktop/HOSPITAL/emp.jpg")

# Create a Tkinter-compatible image object
photo = ImageTk.PhotoImage(image)

# Get the width and height of the image
width, height = image.size

# Create a canvas with the same size as the image
canvas = tk.Canvas(root, width=width, height=height)

# Place the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Create a label with transparent background
label = tk.Label(canvas, text="Employee ID", bg="white", fg="black")
label.config(font=("Arial", 12))
label.place(relx=0.8, rely=0.9)

# Pack the canvas
canvas.pack()

# Run the main event loop
root.mainloop()
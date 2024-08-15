import tkinter as tk
from tkinter import messagebox


def register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    hobbies = [hobby.get() for hobby in hobbies_vars if hobby.get()]
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return
    
    # Print registration details
    print("Username:", username)
    print("Password:", password)
    print("Email:", email)
    print("Gender:", gender)
    print("Hobbies:", hobbies)
    
    messagebox.showinfo("Success", "Registration Successful")

root = tk.Tk()
root.title("Registration Form")

# Username
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)
address_entry = tk.Entry(root, width=100)

# Password
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Confirm Password
confirm_password_label = tk.Label(root, text="Confirm Password:")
confirm_password_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
confirm_password_entry = tk.Entry(root, show="*")
confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

import tkinter as tk

def submit():
    address = address_entry.get()
    print("Address submitted:", address)



# Create and place widgets
address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

address_entry = tk.Entry(root, width=100)
address_entry.grid(row=3, column=1, padx=10, pady=5)


# Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1, padx=10, pady=5)

#Year
label_list = tk.Label(root, text="Select year")
label_list.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
list_items = ["FE", "SE", "TE","BE"]
listbox = tk.Listbox(root)
for item in list_items:
    listbox.insert(tk.END, item)
listbox.grid(row=5, column=1, columnspan=1, padx=10, pady=5)


# Gender
gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
gender_var = tk.StringVar()
gender_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_male.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)
gender_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_female.grid(row=6, column=2, padx=10, pady=5, sticky=tk.W)

# Hobbies
hobbies_label = tk.Label(root, text="Hobbies:")
hobbies_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
hobbies_frame = tk.Frame(root)
hobbies_frame.grid(row=7, column=1, columnspan=2, padx=10, pady=5, sticky=tk.W)

hobbies_vars = []
hobbies = ["Reading", "Writing", "Sports", "Music"]

for i, hobby in enumerate(hobbies):
    var = tk.BooleanVar()
    hobbies_vars.append(var)
    check_button = tk.Checkbutton(hobbies_frame, text=hobby, variable=var)
    check_button.grid(row=0, column=i, padx=5, pady=5, sticky=tk.W)

# Register Button
register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

import tkinter as tk


# Create canvas
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.place(x=900,y=350)

# Draw green rectangle
rectangle = canvas.create_rectangle(50, 50, 250, 150, fill="green")

canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.place(x=900,y=100)
# Create a blue triangle on the canvas
triangle_points = [50, 150, 150, 150, 100, 50]  # x, y coordinates of triangle vertices
canvas.create_polygon(triangle_points, fill="blue")


import tkinter as tk

# Set background color
root.configure(bg="lightblue")  # You can change "lightblue" to any color you want

import tkinter as tk

root.mainloop()

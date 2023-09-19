import tkinter as tk
from tkinter import messagebox
import pyperclip

# Sample data (replace with your own)
passwords = {
    "example.com": {
        "username": "your_username",
        "password": "your_password",
    },
    # Add more entries as needed
}

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website and username and password:
        passwords[website] = {"username": username, "password": password}
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def find_password():
    website = website_entry.get()
    if website in passwords:
        username = passwords[website]["username"]
        password = passwords[website]["password"]
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        pyperclip.copy(password)
    else:
        messagebox.showerror("Error", f"No password found for {website}")

# Create the main window
root = tk.Tk()
root.title("Password Manager")

# Create labels
website_label = tk.Label(root, text="Website:")
username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")

# Create entry fields
website_entry = tk.Entry(root)
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")  # Show asterisks for password

# Create buttons
add_button = tk.Button(root, text="Add", command=save_password)
generate_button = tk.Button(root, text="Generate Password")
search_button = tk.Button(root, text="Search", command=find_password)

# Place widgets on the window
website_label.grid(row=0, column=0)
username_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)

website_entry.grid(row=0, column=1)
username_entry.grid(row=1, column=1)
password_entry.grid(row=2, column=1)

add_button.grid(row=3, column=1, sticky="EW")
generate_button.grid(row=2, column=2)
search_button.grid(row=0, column=2)

# Start the Tkinter event loop
root.mainloop()

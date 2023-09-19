import tkinter as tk
from tkinter import messagebox

# Function to calculate love percentage
def calculate_love():
    your_name = entry_your_name.get()
    partner_name = entry_partner_name.get()

    # Make sure both names are entered
    if your_name == "" or partner_name == "":
        messagebox.showerror("Error", "Please enter both names.")
    else:
        love_percentage = hash(your_name + partner_name) % 101
        result_label.config(text=f"Love Percentage: {love_percentage}%")

# Create the main window
window = tk.Tk()
window.title("Love Calculator")

# Create labels
label_your_name = tk.Label(window, text="Your Name:")
label_partner_name = tk.Label(window, text="Partner's Name:")
result_label = tk.Label(window, text="", font=("Helvetica", 18))

# Create entry fields
entry_your_name = tk.Entry(window)
entry_partner_name = tk.Entry(window)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate Love", command=calculate_love)

# Place widgets on the window
label_your_name.grid(row=0, column=0)
entry_your_name.grid(row=0, column=1)
label_partner_name.grid(row=1, column=0)
entry_partner_name.grid(row=1, column=1)
calculate_button.grid(row=2, columnspan=2)
result_label.grid(row=3, columnspan=2)

# Start the Tkinter event loop
window.mainloop()

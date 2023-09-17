#using tkinter 
import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for input
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create and place the buttons on the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Create the Clear button
clear_button = tk.Button(root, text="Clear", padx=20, pady=20, command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

# Create the Evaluate button
eval_button = tk.Button(root, text="=", padx=20, pady=20, command=evaluate)
eval_button.grid(row=5, column=2, columnspan=2)

# Start the main loop
root.mainloop()

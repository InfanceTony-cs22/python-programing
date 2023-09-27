import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack a listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
listbox.pack(pady=10)

# Create an entry field to add tasks
entry = tk.Entry(root, width=40)
entry.pack()

# Create buttons to add and delete tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
add_button.pack(pady=5)
delete_button.pack()

# Run the Tkinter main loop
root.mainloop()

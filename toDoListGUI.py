import tkinter as tk
from tkinter import messagebox

"""Creating a Tkinter window"""
window = tk.Tk()
window.title('To-Do List')

"""Creating a list to store the to-do items"""
tasks = []

"""Creating an add function"""
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

"""Creating a remove function"""

"""Creating an update function"""

"""Creating the GUI elements"""

"""Starting the Tkinter event loop"""
window.mainloop()
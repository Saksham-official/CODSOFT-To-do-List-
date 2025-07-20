import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():    #add button
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        tasks.append(task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input error", "Pleae enter a task")

def delete_task():    #delete button
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)    #delete from inside also
    else:
        messagebox.showwarning("Selection error","Please select a task to delete")

root = tk.Tk()
root.title("To-do list app using Python")
root.geometry("500x500")

entry = tk.Entry(root, width = 30, font=("Arial", 12))
entry.pack(pady = 10)

#task button
add_btn = tk.Button(root, text="Add task", command = add_task, width = 20, bg = "cyan", fg = "white")
add_btn.pack()

#it show task
listbox = tk.Listbox(root, width = 40, height = 10, font = ("Arial", 12))
listbox.pack(pady = 10)

#delete button
delete_btn = tk.Button(root, text = "Delete selected task", command = delete_task, width = 20, bg = "red", fg = "white")
delete_btn.pack()

root.mainloop() #loop

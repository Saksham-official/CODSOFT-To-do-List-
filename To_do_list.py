import tkinter as tk
from tkinter import messagebox

tasks = []

#add button
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        tasks.append(task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input error", "Please enter a task")

#delete button
def delete_task():
    selected_indices = listbox.curselection()
    if selected_indices:
        index = selected_indices[0]
        listbox.delete(index)
        tasks.pop(index)
    else:
        messagebox.showwarning("Selection error", "Please select a task to delete")

#update button
def update_task():
    selected_indices = listbox.curselection()
    if selected_indices:
        index = selected_indices[0]
        updated_task = entry.get()
        if updated_task:
            tasks[index] = updated_task
            listbox.delete(index)
            listbox.insert(index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "The entry box is empty. Cannot update.")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

#GUI
root = tk.Tk()
root.title("To-do list app using Python")
root.geometry("500x500")
root.configure(bg="#F0F0F0")

#TITLE
title_font = ("Helvetica", 24, "bold")
title_label = tk.Label(root, text="My To-Do List", font=title_font, bg="#F0F0F0", fg="#333")
title_label.pack(pady=(20, 10))

#INPUT FRAME AND WIDGETS
input_frame = tk.Frame(root, bg="#F0F0F0")
input_frame.pack(pady=10)

entry = tk.Entry(input_frame, width=35, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5, ipady=4) # ipady adds vertical padding inside the widget

add_btn = tk.Button(input_frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
add_btn.pack(side=tk.LEFT, ipady=2)

#LISTBOX FRAME
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

listbox = tk.Listbox(listbox_frame, width=40, height=10, font=("Arial", 12), relief=tk.FLAT, selectbackground="#A6A6A6")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#scrollbar
scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#BUTTONS
action_button_frame = tk.Frame(root, bg="#F0F0F0")
action_button_frame.pack(pady=10)

update_btn = tk.Button(action_button_frame, text="Update Selected", command=update_task, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"))
update_btn.pack(side=tk.LEFT, padx=10)

delete_btn = tk.Button(action_button_frame, text="Delete Selected", command=delete_task, bg="#f44336", fg="white", font=("Helvetica", 10, "bold"))
delete_btn.pack(side=tk.LEFT, padx=10)

root.mainloop()
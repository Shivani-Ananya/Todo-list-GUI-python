import tkinter as tk
from tkinter import messagebox
import json
import os

if not os.path.exists("todo_list.json"):
    with open("todo_list.json", "w") as file:
        json.dump([], file)

def load_tasks():
    with open("todo_list.json", "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("todo_list.json", "w") as file:
        json.dump(tasks, file, indent=2)

def add_task():
    task_test = task_entry.get().strip()
    if task_test == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    tasks = load_tasks()
    new_task = {"task": task_test, "status": False}
    tasks.append(new_task)
    save_tasks(tasks)

    update_task_listbox()
    task_entry.delete(0, tk.END)

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    tasks = load_tasks()

    for i, task in enumerate(tasks, start=1):
        status = "(Done)" if task["status"] else "(Not Done)"
        task_listbox.insert(tk.END, f"[{i}] {status} {task['task']}")

def mark_done():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")
        return

    index = selected_index[0]
    tasks = load_tasks()
    tasks[index]["status"] = True
    save_tasks(tasks)
    update_task_listbox()

def delete_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Warning", "Please select a task to delete!")
        return

    index = selected_index[0]
    tasks = load_tasks()

    confirm = messagebox.askyesno("Confirm Deletion", f"Delete task: {tasks[index]['task']}?")
    if confirm:
        tasks.pop(index)
        save_tasks(tasks)
        update_task_listbox()

root = tk.Tk()
root.title("Ananya's To-Do List")
root.geometry("400x480")
root.config(bg="#f2f2f2")

title_label = tk.Label(root, text="`My To-Do List", font=("Helvetica", 18, "bold"), bg="#f2f2f2")
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=15, font=("Helvetica", 12))
task_listbox.pack(pady=10)

done_button = tk.Button(root, text="Mark as Done", width=20, command=mark_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

update_task_listbox()

root.mainloop()

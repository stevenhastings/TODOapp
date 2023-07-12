from datetime import datetime
import tkinter as tk
import tkinter.messagebox

user_prompt = "Enter a todo: "
current_date = datetime.today().strftime('%Y-%m-%d')

def read_todos():
    try:
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        return todos
    except IOError:
        print("An error occurred while reading the todos file.")
        return []

def write_todos(todos):
    with open("todos.txt", "w") as file:
        file.writelines(todos)

def add_todo():
    todo = entry.get()
    if todo:
        todos = read_todos()
        todos.append(f"{todo} @ {current_date}\n")
        write_todos(todos)
        listbox.insert(tk.END, f"{len(todos)}. {todo}")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Todo", "Please enter a todo.")

def remove_todo():
    selected_indices = listbox.curselection()
    if selected_indices:
        todos = read_todos()
        for index in reversed(selected_indices):
            todos.pop(index)
            listbox.delete(index)
        write_todos(todos)
    else:
        messagebox.showwarning("No Selection", "Please select a todo to remove.")

def clear_todos():
    confirmed = messagebox.askyesno("Clear Todos", "Are you sure you want to clear all todos?")
    if confirmed:
        write_todos([])
        listbox.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Todo List")

# Create the listbox to display todos
listbox = tk.Listbox(window)
listbox.pack(pady=10)

# Populate the listbox with existing todos
todos = read_todos()
for index, todo in enumerate(todos, start=1):
    listbox.insert(tk.END, f"{index}. {todo.strip()}")

# Create the entry field for adding todos
entry = tk.Entry(window)
entry.pack(pady=5)

# Create the Add Todo button
add_button = tk.Button(window, text="Add Todo", command=add_todo)
add_button.pack(pady=5)

# Create the Remove Todo button
remove_button = tk.Button(window, text="Remove Todo", command=remove_todo)
remove_button.pack(pady=5)

# Create the Clear Todos button
clear_button = tk.Button(window, text="Clear Todos", command=clear_todos)
clear_button.pack(pady=5)

# Start the main event loop
window.mainloop()

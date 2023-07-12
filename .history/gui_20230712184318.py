import PySimpleGUI as sg
import funcs

def create_gui():
    layout = [
        [sg.InputText(key="-TODO-"), sg.Button("Add Todo", key="-ADD-")],
        [sg.Listbox(values=funcs.get_todo_list(), key="-TODOLIST-", size=(40, 10))],
        [sg.Button("Remove Todo", key="-REMOVE-"), sg.Button("Clear Todos", key="-CLEAR-")]
    ]

    window = sg.Window("Todo List", layout)

    layout.append([sg.Button])

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        
        if event == "-ADD-":
            todo = values["-TODO-"]
            if todo:
                funcs.add_todo(todo)
                window["-TODOLIST-"].update(values=funcs.get_todo_list())
                window["-TODO-"].update("")
            else:
                sg.popup("Empty Todo", "Please enter a todo.")
        
        if event == "-REMOVE-":
            selected_indices = values["-TODOLIST-"]
            if selected_indices:
                todos = [window["-TODOLIST-"].get(idx) for idx in selected_indices]
                for todo in todos:
                    funcs.remove_todo(todo)
                window["-TODOLIST-"].update(values=funcs.get_todo_list())
            else:
                sg.popup("No Selection", "Please select a todo to remove.")
        
        if event == "-CLEAR-":
            confirmed = sg.popup_yes_no("Clear Todos", "Are you sure you want to clear all todos?")
            if confirmed == "Yes":
                funcs.clear_todos()
                window["-TODOLIST-"].update(values=[])

        if event == "-EDIT-":
            todo = values["-TODOLIST-"][0]
            new_todo = sg.popup_get_text("Enter the updated todo:", default_text=todo)
            if new_todo:
                if funcs.edit_todo(todo, new_todo):
                    window["-TODOLIST-"].update(values=funcs.get_todo_list())
                else:
                    sg.popup("Todo not found.", "Please try again.")

    window.close()

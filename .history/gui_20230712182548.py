import funcs
import sys
import os
import PySimpleGUI as sg 

# Define the window's contents
layout = [[sg.Text("What would you like to do?")],
            [sg.Input(key='-INPUT-')],
            [sg.Button('Add'), 
             sg.Button('Remove'), 
             sg.Button('Show'), 
             sg.Button('Clear'), 
             sg.Button('Edit'), 
             sg.Button('Complete'), 
             sg.Button('Exit')]]

# Create the window
window = sg.Window('Todo List', layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Exit button
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Add':
        funcs.add_todo()
    if event == 'Remove':
        funcs.remove_todo()
    if event == 'Show':
        funcs.show_todos()
    if event == 'Clear':
        funcs.clear_todos()
    if event == 'Edit':
        funcs.edit_todo()
    if event == 'Complete':
        funcs.complete_todo()

window.close()

# # Define the window's contents
# layout = [[sg.Text("What would you like to do?")],
#             [sg.Input(key='-INPUT-')],
#             [sg.Button('Add'),
#              sg.Button('Remove'),
#              sg.Button('Show'),

    



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
    



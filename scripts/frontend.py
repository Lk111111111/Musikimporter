from os import name
from tkinter import Menu

import PySimpleGUI as sg

sg.theme("Dark Grey 15")
layout = [
    [sg.Text("Enter Artist here"), sg.InputText(key="-ARTIST-")],
    [sg.Button("Ok", bind_return_key=True), sg.Button("Cancel")],
    [sg.Text("Slider"), sg.Slider(range=(0, 100), orientation="h", key="-SLIDER-")],
]

window = sg.Window("Musikimporter", layout)

while True:
    """Window Loop"""
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    if event == "Ok":
        import main as app  # <- replace with your file name (without .py)

        app.main(values)  # pass the current GUI values
        continue  # keep the window open

window.close()

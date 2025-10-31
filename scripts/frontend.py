import PySimpleGUI as sg

sg.theme("Dark Grey 15")
layout = [
    [sg.Text("Enter Artist here"), sg.InputText(key="-ARTIST-")],
    [sg.Button("Ok"), sg.Button("Cancel")],
]

window = sg.Window("Musikimporter", layout)

while True:
    """Window Loop"""
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    if event == "Ok":
        break

    print("You entered ", values[0])

window.close()

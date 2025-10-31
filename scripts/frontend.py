import PySimpleGUI as sg

# --- Einfaches Fenster zur Artist-Eingabe ---
layout = [
    [sg.Text("Please enter the artist")],
    [sg.Input(key="-ARTIST-")],
    [sg.Button("Ok")],
]
window = sg.Window("Artist Search", layout)
event, values = window.read()
window.close()
# -------------------------------------------

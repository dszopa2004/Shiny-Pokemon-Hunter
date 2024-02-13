import tkinter as tk
from tkinter import *
import main as app
import sys
import json


# Gets the encounters from main
def get_encounters():
    return app.encounters


# This function updates the encounters label
# To accurately match the current number of encounters
def update_encounters():
    global encounters_label
    encounters = get_encounters()

    encounters_label.config(text="Encounters: " + str(encounters))
    encounters_label.after(1000, update_encounters)


# This function saves the current encounters to the json
def save_encounters():
    file = open('encounters.json')
    data = json.load(file)

    prev_encounters = data["encounters"]
    file.close()

    curr_encounters = get_encounters()

    total_encounters = prev_encounters + curr_encounters

    dictionary = {
        "encounters": total_encounters
    }

    with open('encounters.json', 'w') as json_file:
        json.dump(dictionary, json_file)


# This function is used to close the program
# The player will continue to move in the same direction
# Until the same corressponding directional movement key is pressed
def close():
    app.stop_flag = True
    print("Exiting Program.")
    sys.exit()


# Creates the GUI menu with Tkinter
def menu():
    global encounters_label
    root = tk.Tk()
    root.title("Shiny Hunter")
    root.geometry("400x300+300+120")

    start_btn = tk.Button(root, text="Start", width=25, command=app.main)
    stop_btn = tk.Button(root, text="Stop", width=25, command=close)
    save_btn = tk.Button(root, text="Save", width=25, command=save_encounters)
    encounters_label = tk.Label(root, text="Encounters: 0")

    start_btn.pack()
    stop_btn.pack()
    encounters_label.pack()
    save_btn.pack()

    update_encounters()

    root.mainloop()


menu()
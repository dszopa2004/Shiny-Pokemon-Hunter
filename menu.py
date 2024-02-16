import tkinter as tk
from tkinter import *
import main as app
import save as save


# Gets the encounters from main
def get_encounters():
    return app.encounters


# This function updates the encounters label
# To accurately match the current number of encounters
def update_encounters():
    global encounters_label
    encounters = get_encounters()

    encounters_label.config(text="Current Encounters: " + str(encounters))
    encounters_label.after(1000, update_encounters)


# Creates the GUI menu with Tkinter
def menu():
    global encounters_label
    global total_encounters_label
    root = tk.Tk()
    root.title("Shiny Hunter")
    root.geometry("400x300+300+120")

    start_btn = tk.Button(root, text="Start", width=25, command=app.main)
    save_btn = tk.Button(root, text="Save & Exit", width=25, command=save.save_encounters)
    encounters_label = tk.Label(root, text="Current Encounters: 0")
    total_encounters_label = tk.Label(root, text="Total Saved Encounters: 0")

    start_btn.pack()
    encounters_label.pack()
    total_encounters_label.pack()
    save_btn.pack()

    update_encounters()
    save.load_encounters(total_encounters_label)

    root.mainloop()


menu()
import tkinter as tk
import main as app
import sys


# This function is used to close the program
# The player will continue to move in the same direction
# Until the same corressponding directional movement key is pressed
def close():
    app.stop_flag = True
    print("Exiting Program.")
    sys.exit()

# Creates the GUI menu with Tkinter
def menu():
    root = tk.Tk()
    root.title("Shiny Hunter")
    root.geometry("400x300+300+120")

    start_btn = tk.Button(root, text="Start", width=25, command=app.main)
    stop_btn = tk.Button(root, text="Stop", width=25, command=close)

    start_btn.pack()
    stop_btn.pack()

    root.mainloop()


menu()
import tkinter as tk
import main as app
import sys

def close():
    app.stop_flag = True
    print("Exiting Program.")
    sys.exit()

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
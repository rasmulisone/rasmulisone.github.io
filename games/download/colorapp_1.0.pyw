from colorutils import random_web
import tkinter as tk

autochanging = False
bpm = 120
delay = 500

def change():
    color = random_web()
    window.configure(bg=color)
    white.configure(text=color, background=color)
    black.configure(text=color, background=color)

def copy():
    window.clipboard_clear()
    toCopy = str(window["background"]).replace("#", "")
    window.clipboard_append(toCopy)

def autochange():
    if(autochanging):
        change()
        window.after(int(delay), autochange)

def autochangeControl():
    global autochanging
    global bpm
    global delay
    try:
        bpm = int(bpmEntry.get())
        delay = int((60 / bpm) * 1000)
        if(autochanging):
            autochanging = False
        else:
            autochanging = True
            autochange()
    except ValueError:
        bpmEntry.delete(0, "end")

window = tk.Tk()
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=8)
window.rowconfigure(1, weight=8)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(5, weight=1)
window.wm_title("Color App 1.0")
window.geometry("320x200")
window.minsize(width="320", height="220")
white = tk.Label(window, fg="white", font=("Arial", 25))
black = tk.Label(window, font=("Arial", 25))
white.grid(row=0, columnspan=2)
black.grid(row=1, columnspan=2)
change()
copyButton = tk.Button(window, text="Copy code", command=copy)
copyButton.grid(row=2, columnspan=2, sticky=("N", "S", "E", "W"))
button = tk.Button(window, text="Change color", command=change)
button.grid(row=3, columnspan=2, sticky=("N", "S", "E", "W"))
tk.Label(window, text="Colors per minute", bg="#FFFFFF").grid(row=4, column=0, sticky=("N", "S", "W"))
bpmEntry = tk.Entry(window)
bpmEntry.grid(row=4, column=1, sticky=("N", "S", "E", "W"), columnspan=2)
autoButton = tk.Button(window, text="Autochange", command=autochangeControl)
autoButton.grid(row=5, columnspan=2, sticky=("N", "S", "E", "W"))
tk.Label(window, text="Color App 1.0 for Python - (C) 2018 Rasmulisone Games", bg="#FFFFFF").grid(row=6, column=0, columnspan=2, sticky=("N", "S", "E", "W"))
window.mainloop()

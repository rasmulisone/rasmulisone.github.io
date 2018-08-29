from colorutils import random_web
import tkinter as tk

def change():
    color = random_web()
    frame.configure(bg=color)
    white.configure(text=color, background=color)
    black.configure(text=color, background=color)

def copy():
    window.clipboard_clear()
    toCopy = str(frame["background"]).replace("#", "")
    window.clipboard_append(toCopy)

window = tk.Tk()
window.wm_title("Color App 0.2 beta")
window.geometry("320x150")
window.minsize(width="320", height="150")
window.maxsize(width="1000", height="200")
frame = tk.Frame(window)
frame.pack(fill="both", expand=True)
white = tk.Label(frame, fg="white", font=("Arial", 25))
black = tk.Label(frame, font=("Arial", 25))
white.pack()
black.pack()
change()
copyButton = tk.Button(frame, text="Copy code", command=copy)
copyButton.pack(fill="both", expand=True)
button = tk.Button(frame, text="Change color", command=change)
button.pack(side="bottom", fill="both", expand=True)
window.mainloop()

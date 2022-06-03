import random
import tkinter as tk


app = tk.Tk()
app.geometry("200x220")

label = tk.Label(app, text="0")
label.pack()

def change(b=0):
    if b < 30:
        a = random.randrange(1, 7, 1)
        label.config(text=a)
        app.after(100, change, b+1)


b1 = tk.Button(app, text="Get New Number", command=change)
b1.pack()


app.mainloop()
import tkinter as tk
from time import strftime
from tkinter import *
from tkinter import ttk
import datetime as dt
from PIL import Image, ImageTk
from PIL import ImageTk, Image

date = dt.datetime.now()




def dark_theme():
    frame = tk.Frame(root, bg="#111d33")
    
    frame.place(relx=0.0001, rely=0.0001, relwidth=1, relheight=1)
    
    lbl_2 = tk.Label(frame, font=('Steamwreck', 50),
                     background='#111d33', foreground='#ea871e')
    lbl_2.pack(anchor="center")
    
    test2 = tk.Label(frame, text=f"{date:%A, %B %d, %Y}", font=('Steamwreck', 30),
                     background='#111d33', foreground='#ea871e')
    test2.pack(anchor="s")

    def time():
        string = strftime('%I:%M:%S %p')
        lbl_2.config(text=string)
        lbl_2.after(1000, time)
    time()





root = tk.Tk()

root.iconbitmap(r'C:\Users\Elias Diamond\OneDrive\Documents\Clock py\Clock icon.ico')

root.title("Digital Steampunk Clock")

canvas = tk.Canvas(root, height=140, width=400)

canvas.pack()


frame = tk.Frame(root, bg='#111d33')

frame.place(relx=0.0001, rely=0.0001, relwidth=1, relheight=1)

lbl = tk.Label(frame, font=('Steamwreck', 50),
                     background='#111d33', foreground='#ea871e')
lbl.pack(anchor="center")

test3 = tk.Label(frame, text=f"{date:%A, %B %d, %Y}", font=('Steamwreck', 30),
                     background='#111d33', foreground='#ea871e')
test3.pack(anchor="s")

Cr = tk.Label(frame, text="Oringnal code by AdityaJ7\nSteampunk version by SteamWolf", font=('Steamwreck', 20),
                     background='#111d33', foreground='#ea871e')
Cr.pack(anchor="s")







def time():
    string = strftime('%I:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
time()
    

root.mainloop()
import pyautogui, PIL, webcolors
import tkinter as tk
from threading import Thread

def cursorpixel():
    x,y = pyautogui.position()
    pixel = (x,y,x+1,y+1)
    grabColor(pixel)

def grabColor(square, max_colors=256):
    global color_label,root
    img=PIL.ImageGrab.grab(square)
    color = img.getcolors(max_colors)
    maxocc, mostpres = 0, 0
    for c in color:
        if c[0] > maxocc:
            (maxocc, mostpres) = c
    givencolor = getcolor(mostpres)
    color_label.config(text=givencolor)

def getcolor(x):
    minclr = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_r, g_r, b_r = webcolors.hex_to_rgb(key)
        rd = (r_r - x[0]) ** 2
        gd = (g_r - x[1]) ** 2
        bd = (b_r - x[2]) ** 2
        minclr[(rd + gd + bd)] = name
    col = minclr[min(minclr.keys())]
    return col

def refresh():
    while True:
        cursorpixel()

global color_label,root
root=tk.Tk()
root.minsize(150, 50)
color_label = tk.Label(root)
color_label.config(font=("Arial", 20))
color_label.pack()
Thread(target=refresh).start()
root.mainloop()

import tkinter as tk
from tkinter import TOP, LEFT
from tkinter.ttk import *
from calc_logic import main_function as main

r = tk.Tk()

# creating the window, title, icon of the calculator
r.title('Voice Calculator')
r.geometry('700x300')
# r.eval('tk::PlaceWindow . center') # placing the window on the center
p1 = tk.PhotoImage(file='images.png')
r.iconphoto(False, p1)

# creating the button with the image
# Adding widgets to the root window
Label(r, text='Voice Button', font=('Verdana', 12)).pack(side=TOP, pady=10)
# Creating a photo-image object to use image
photo = tk.PhotoImage(file="m1.png")
# Resizing image to fit on button
photoimage = photo.subsample(3, 3)
Button(r, text='Click Me !', image=photoimage, compound=LEFT, command=main).pack(side=TOP)

Button(r, text='Quit', command=r.destroy).pack(side=TOP, pady=10)
r.mainloop()

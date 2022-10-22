import tkinter as tk
from tkinter import TOP, LEFT
from tkinter import *
# from tkinter.ttk import *   MG remove this lib
from turtle import down
from calc_logic import main_function as main
from calc_logic import xinput
from calc_logic import *

r = tk.Tk()

# GUI Configurations
r.title('Voice Calculator')
r.config(bg='#F5F5DC')  # Colors
r.resizable(0, 0)  # Remove Resize button
r.geometry('350x550')
p1 = tk.PhotoImage(file='images.png')
r.iconphoto(False, p1)
# --------

# creating the button with the image
# Adding widgets to the root window

Label(r, text='Press the Button', font=(
    'Verdana', 16, 'bold'), bg='#F5F5DC', fg='#33A1C9').pack(side=TOP, pady=10)
# Creating a photo-image object to use image
photo = tk.PhotoImage(file="mic.png")

photoimage = photo.subsample(3, 3)  # Resizing image to fit on button

b1 = Button(r, image=photoimage, compound=LEFT,
            command=main, bg='#F5F5DC', borderwidth=0)
b1.pack(side=TOP)
# -----// Example Statement
Label(r, text="Say what you want to calculate, example: 3 plus 3",
      font=('Ariel', 10, 'bold'), bg='#F5F5DC').pack()
# --- // OUTPUT IN GUI
l1 = Label(r, text=xinput, font=(
    'Verdana', 16, 'bold'),  bg='#FFC0CB')
l1.pack(pady=33)
l2 = Label(r, text=xoutput, font=(
    'Verdana', 16, 'bold'),  bg='#FFC0CB')
l2.pack(pady=33)
# ---
b2 = Button(r, text='Quit', bg='#DC143C', fg='#FFFFFF', command=r.destroy)
b2.pack(side=BOTTOM, pady=10)
# ----- GUI END---------


r.mainloop()

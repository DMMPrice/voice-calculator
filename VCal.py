from tkinter import *
from tkinter import Canvas

r1 = Tk()
r1.resizable(0, 0)  # Remove Resize button
r1.title('Voice Calculator')
r1.config(bg='Lightgoldenrod1')
r1.geometry('350x550')  # Size of the Frame
r1.eval('tk::PlaceWindow . center')  # To Always display windows in center

# Test Code
p1 = PhotoImage(file='m1.png')
r1.iconphoto(False, p1)

r1.mainloop()

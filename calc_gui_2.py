import tkinter as tk
from tkinter import *

# Creating the root window
r = tk.Tk()

# GUI Configurations
r.title('Voice Calculator')
# r.config(bg='#F5F5DC')  #Colors
r.resizable(0, 0)  # Remove Resize button
r.geometry('350x550')
# r.eval('tk::PlaceWindow . center') # Placing the window in the center
p1 = tk.PhotoImage(file='images.png')
r.iconphoto(False, p1)

# Creating a frame
frame1 = Frame(r)
frame1.pack(side="top", expand=True, fill="both")
frame2 = Frame(r)
frame2.pack(expand=True, fill="both")


# --------
def callingFunction():
    import calc_logic as calc
    # test_speech = Label(frame2, text="Please wait", font=('Verdana', 16, 'bold'))
    # test_speech.pack(pady=33)
    output_file = calc.main_function()
    # test_speech = Label(frame2, text="Say", font=('Verdana', 16, 'bold'))
    # test_speech.pack(pady=33)
    # Displaying the voice output
    voiceOutput = Label(frame2, text=str(output_file[0]), font=('Verdana', 16, 'bold'))
    voiceOutput.pack(pady=33)

    # Displaying the evaluated output
    evalOutput = Label(frame2, text=str(output_file[1]), font=('Verdana', 16, 'bold'))
    evalOutput.pack(pady=33)
    Button(frame2, text="Clear", font=('Helvetica bold', 10), command=clear_frame).pack(pady=20)


# Creating a clear frame
def clear_frame():
    for widgets in frame2.winfo_children():
        widgets.destroy()


# Creating a photo-image object to use image
photo = tk.PhotoImage(file="mic.png")
photoImage = photo.subsample(3, 3)  # Resizing image to fit on button

# creating the button with the image
voiceButton = Button(frame1, image=photoImage, compound=LEFT, command=callingFunction, borderwidth=0)
voiceButton.pack(side=TOP)

egStatement = Label(frame1, text="Say what you want to calculate, example: 13 plus 63", font=('Ariel', 10, 'bold'))
egStatement.pack()

voiceLabel = Label(frame1, text='Press the Button', font=('Verdana', 16, 'bold'), fg='#33A1C9')
voiceLabel.pack(pady=10)

# Creating the exit button
exitButton = Button(r, text='Quit', bg='#DC143C', fg='#FFFFFF', command=r.destroy)
exitButton.pack(side=BOTTOM, pady=10)

r.mainloop()

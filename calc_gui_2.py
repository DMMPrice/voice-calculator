import tkinter as tk
from tkinter import *

# Creating the root window
r = tk.Tk()

# GUI Configurations
r.title('Voice Calculator')
r.config(bg='#F5F5DC')  # Colors
r.resizable(0, 0)  # Remove Resize button
r.geometry('350x550')
p1 = tk.PhotoImage(file='images.png')
r.iconphoto(False, p1)

# Creating a frame
frame1 = Frame(r)
frame1.pack(side="top", expand=True, fill="both")


# --------
def callingFunction():
    import calc_logic as calc
    output_file = calc.main_function()

    # Displaying the voice output
    voiceOutput = Label(frame1, text=str(output_file[0]), font=(
        'Verdana', 16, 'bold'))
    voiceOutput.pack(pady=33)

    # Displaying the evaluated output
    evalOutput = Label(frame1, text=str(output_file[1]), font=(
        'Verdana', 16, 'bold'))
    evalOutput.pack(pady=33)
    Button(frame1, text="Clear", font=('Helvetica bold', 10), command=clear_frame).pack(pady=20)


# Creating a clear frame
def clear_frame():
    for widgets in frame1.winfo_children():
        widgets.destroy()


# creating the button with the image
# Adding widgets to the root window


# Creating a photo-image object to use image
photo = tk.PhotoImage(file="mic.png")
photoImage = photo.subsample(3, 3)  # Resizing image to fit on button
voiceButton = Button(r, image=photoImage, compound=LEFT, command=callingFunction, bg='#F5F5DC', borderwidth=0)
voiceButton.pack(side=TOP)

egStatement = Label(r, text="Say what you want to calculate, example: 13 plus 63",
                    font=('Ariel', 10, 'bold'), bg='#F5F5DC')
egStatement.pack()

voiceLabel = Label(r, text='Press the Button', font=(
    'Verdana', 16, 'bold'), bg='#F5F5DC', fg='#33A1C9')
voiceLabel.pack(pady=10)

exitButton = Button(r, text='Quit', bg='#DC143C', fg='#FFFFFF', command=r.destroy)
exitButton.pack(side=BOTTOM, pady=10)

r.mainloop()

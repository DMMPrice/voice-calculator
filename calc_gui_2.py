from tkinter import *
import tkinter as tk

# Creating the root window
r = tk.Tk()

# GUI Configurations
r.title('Voice Calculator')
# r.resizable(0, 0)  # Remove Resize button
r.geometry('450x700')
r.config(bg='#470B48')
r.iconbitmap(r'Voice.ico')

# Creating a frame
frame1 = Frame(r, bg='#470B48')
frame1.config(pady=20)
frame1.pack(side="top", fill="both")
frame2 = Frame(r, bg='#470B48')
frame1.config(pady=20)
frame2.pack(fill="both")


# --------
def callingFunction():
    import calc_logic as calc
    # test_speech = Label(frame2, text="Please wait", font=('Verdana', 16, 'bold'))
    # test_speech.pack(pady=33)
    output_file = calc.main_function()
    # test_speech = Label(frame2, text="Say", font=('Verdana', 16, 'bold'))
    # test_speech.pack(pady=33)
    # Displaying the voice output
    voiceOutput = Label(frame2, text=str(output_file[0]), font=('Verdana', 16, 'bold'), fg="#E7F922", bg='#470B48')
    voiceOutput.pack(pady=33)

    # Displaying the evaluated output
    evalOutput = Label(frame2, text=str(output_file[1]), font=('Verdana', 16, 'bold'), fg="#E7F922", bg='#470B48')
    evalOutput.pack(pady=33)
    Button(frame2, text="Clear", font=('Sans Serif', 16), command=clear_frame, bg='#FB1D1D', fg='#EEE3E3', border=0,
           borderwidth=0, cursor='hand2').pack(
        pady=20)


# Creating a clear frame
def clear_frame():
    for widgets in frame2.winfo_children():
        widgets.destroy()


# Creating a photo-image object to use image
welcomeStatement = Label(frame1, text="Welcome to the Voice Calculator", font=('Ariel', 20),
                         bg='#470B48', fg="#DDED2A")
photo = tk.PhotoImage(file="mic.png")
photoImage = photo.subsample(4, 4)  # Resizing image to fit on button

# creating the button with the image
voiceButton = Button(frame1, image=photoImage, compound=LEFT, command=callingFunction, borderwidth=0, bg='#470B48',
                     activebackground='#911294')
voiceButton.config(cursor='hand2')
egStatement = Label(frame1, text="Say what you want to calculate \n Example: 13 plus 63", font=('Ariel', 15, 'bold'),
                    bg='#470B48', fg="white")
voiceLabel = Label(frame1, text='Press the Button', font=('Verdana', 18, 'bold'), fg='#27A0E4', bg='#470B48')
welcomeStatement.pack(pady=5)
voiceButton.pack(side=TOP)
egStatement.pack()
voiceLabel.pack(pady=10)

# Creating the exit button
exitButton = Button(r, text='Quit', bg='#470B48', fg='#DD1010', font=('Sans Serif', 15), command=r.destroy)
exitButton.config(borderwidth=5, border=0, cursor='hand2')
exitButton.pack(side=BOTTOM, pady=10, padx=10)

r.mainloop()

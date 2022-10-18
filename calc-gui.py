import tkinter as tk

r = tk.Tk()
r.title('Voice Calculator')
r.geometry('700x300')
# click_btn=
voiceButton = tk.Button(r, width=15, text='click me', command=r.destroy)
voiceButton.pack()
r.mainloop()

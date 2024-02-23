from tkinter import *

windows = Tk()

windows.minsize(500, 300)
windows.title("First GUI")
windows.config(padx=20, pady=20)

def click_me():
    label.config(text=input.get())
    
label = Label(text="Halo ini Rama", font=("Arial", 24, "bold"))

label.grid(column=1, row=0)

button = Button(text="Pencet Aku Gan", command=click_me)

button.grid(column=0, row = 1)


new_button = Button(text="Pencet Aku Gan", command=click_me)

new_button.grid(column=2, row=1)

input = Entry()

input.grid(column=1, row=2)


windows.mainloop()
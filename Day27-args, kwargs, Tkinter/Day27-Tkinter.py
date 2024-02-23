from tkinter import *

def convert_value():
    new_value = round(int(input.get()) * 1.60934)
    value['text'] = new_value

windows = Tk()

windows.minsize(200, 100)
windows.title("Mile to Km Converter")
windows.config(padx=20, pady=20)

input = Entry(width=10)

input.grid(column=1, row=0)

label = Label(text="Miles", font=("Arial", 10, "bold"))

label.grid(column=2, row=0)

label_2 = Label(text="Is Equal To", font=("Arial", 10, "bold"))

label_2.grid(column=0, row=1)

value = Label(text=0, font=("Arial", 10, "bold"))

value.grid(column=1, row=1)

label_3 = Label(text="Km", font=("Arial", 10, "bold"))

label_3.grid(column=2, row=1)

button = Button(text="Convert", command=convert_value)

button.grid(column=1, row=2)

# def click_me():
#     label.config(text=input.get())

# button = Button(text="Pencet Aku Gan", command=click_me)

# button.pack()







windows.mainloop()
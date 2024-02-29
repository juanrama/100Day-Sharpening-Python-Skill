from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

###Data
pd = pandas
word = {}
lang_dict = {}

try:
    data = pd.read_csv("data/to_learn.csv")
except:
    ori_data = pd.read_csv("data/french_words.csv")
    lang_dict = ori_data.to_dict(orient="records")
else: 
    lang_dict = data.to_dict(orient="records")
    
word = random.choice(lang_dict)

###Command button
def next_lang():
    global word, flip_card
    window.after_cancel(flip_card)
    word = random.choice(lang_dict)
    card.itemconfig(card_image, image = card_img)
    card.itemconfig(card_title, text = "French", fill = "black")
    card.itemconfig(card_word, text = word['French'], fill = "black" )
    flip_card = window.after(3000, flip_english)
    print(len(lang_dict))

def is_known():
    global lang_dict
    lang_dict.remove(word)
    pd.DataFrame(lang_dict).to_csv("to_learn.csv", index=False, header=False)
    next_lang()
    

def flip_english():
    global word
    card.itemconfig(card_image, image = card_back_img)
    card.itemconfig(card_title, text = "English", fill = "white")
    card.itemconfig(card_word, text = word['English'], fill = "white")
    

### UI
window = Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
card_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

##CARD
card = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_image = card.create_image(400, 263, image = card_img)
card_title = card.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = card.create_text(400, 263, text=word['French'], font=("Ariel", 60, "bold"), tags="french_text")
card.grid(column=0, row=0, columnspan=2)


##BUTTON
right_img = PhotoImage(file="images/right.png")
right = Button(image=right_img, highlightthickness=0, command=is_known)
right.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, command=next_lang)
wrong.grid(row=1, column=0)

flip_card = window.after(3000, flip_english)


window.mainloop()



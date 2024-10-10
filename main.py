from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data =pandas.read_csv("data/french_words.csv")
to_learn=data.to_dict(orient ="records")
current_card={}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="blue")
    canvas.itemconfig(card_word, text= current_card["French"], fill="blue")
    canvas.itemconfig(card_bg, image=card_fnt_img)
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="red")
    canvas.itemconfig(card_word, text=current_card["English"], fill="red")
    canvas.itemconfig(card_bg, image=card_fnt_img)

def is_known():
    to_learn.remove(current_card)
    data= pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    # print(len(to_learn))
    next_card()

window=Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer= window.after(3000, func=flip_card)

canvas= Canvas(width=800, height=526)
card_back_img = PhotoImage(file= "images/card_back.png")
card_fnt_img = PhotoImage(file= "images/card_back.png")
card_bg= canvas.create_image(400, 263, image = card_back_img)

card_title=canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word= canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img=PhotoImage(file="images/wrong.png")
unknown_btn= Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0 )

check_img=PhotoImage(file="images/right.png")
known_btn=Button(image=check_img, highlightthickness=0, command=is_known)
known_btn.grid(row=1 ,column=1)

next_card()

window.mainloop()
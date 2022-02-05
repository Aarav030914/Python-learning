from tkinter import Button, Canvas, Label, PhotoImage, Tk
import pandas
from random import randint
BACKGROUND_COLOR = "#B1DDC6"
card_state = "front"


# BACKEND

# Reading Data Base and creating a new one
data = pandas.read_csv("./day31/flash-card-project-start/data/words_to_learn.csv")
work_data = data.to_dict()

random_num = randint(0, len(data["French"])-1)
f_word = work_data["French"][random_num]
e_word = work_data["English"][random_num]

french_words = data.French.to_list()
english_words = data.English.to_list()

unk_words = {
    "French" : french_words,
    "English" : english_words
}

# Updating words according to button click
def change_word(check):
    global f_word
    global random_num
    global e_word
    
    if check:
        unk_words["French"].remove(f_word)
        unk_words["English"].remove(e_word)
        pandas.DataFrame(unk_words).to_csv("./day31/flash-card-project-start/data/words_to_learn.csv", index=False)
        print(f_word, e_word)
        
    if card_state == "back":
        flip_card()
    
    random_num = randint(0, len(data["French"])-1)
    f_word = work_data["French"][random_num]
    e_word = work_data["English"][random_num]
    canvas.itemconfig(word, text=f_word)

# Card Flip Mechanism
def flip_card():
    global card_state
    if card_state == "front":
        canvas.itemconfig(bg_img, image=bg_img_b)
        canvas.itemconfig(lang, text="English")
        canvas.itemconfig(word, text=e_word)
        card_state = "back"
    
    else:
        canvas.itemconfig(bg_img, image=bg_img_f)
        canvas.itemconfig(lang, text="French")
        canvas.itemconfig(word, text=f_word) 
        card_state = "front"   


# GUI

# creating window
window = Tk() 
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_img_f = PhotoImage(file="./day31/flash-card-project-start/images/card_front.png")

bg_img_b = PhotoImage(file="./day31/flash-card-project-start/images/card_back.png")

bg_img = canvas.create_image(400, 263, image=bg_img_f)
lang = canvas.create_text(400, 150, text="French", font=("Courier", 40, "italic"))
word = canvas.create_text(400, 263, text=f_word, font=("Courier", 80, "bold"))

canvas.grid(column=0, row=0, columnspan=3)

# Buttons
right_img = PhotoImage(file="./day31/flash-card-project-start/images/right.png")
right = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda : change_word(True))
right.grid(column=0, row=1)

wrong_img = PhotoImage(file="./day31/flash-card-project-start/images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=lambda : change_word(False))
wrong.grid(column=2, row=1)

flip = Button(text="Flip", highlightthickness=0, bg=BACKGROUND_COLOR, command=flip_card)
flip.grid(column=1, row=1)

window.mainloop()
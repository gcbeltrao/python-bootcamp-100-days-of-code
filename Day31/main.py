from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
dictionary = {}


# CREATION OF UNKNOWN WORDS
def remove_known_word():
    dictionary.remove(current_card)
    data = pd.DataFrame(dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)


# SELECT CARDS
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_df = pd.read_csv("data/french_words.csv")
    dictionary = original_df.to_dict(orient="records")
else:
    dictionary = df.to_dict(orient="records")


def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    canvas.itemconfig(background_image, image=card_front_img)
    current_card = random.choice(dictionary)
    french_word = current_card["French"]

    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=french_word, fill="Black")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(background_image, image=card_back_img)
    english_word = current_card["English"]
    canvas.itemconfig(card_title, text="English", fill="White")
    canvas.itemconfig(card_word, text=english_word, fill="White")


# UI
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")

background_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# Buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=lambda: [next_card(), remove_known_word()])
right_button.grid(column=1, row=1)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()

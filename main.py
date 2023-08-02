import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card['French'])


window = tkinter.Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526)
card_front_img = tkinter.PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = tkinter.PhotoImage(file='images/wrong.png')
unknown_button = tkinter.Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = tkinter.PhotoImage(file='images/right.png')
known_button = tkinter.Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()

import tkinter as tk
import random
from tkinter import messagebox

# Game setup
symbols = ['🍎', '🍌', '🍇', '🥝', '🍓', '🍉', '🍍', '🍒'] * 2
random.shuffle(symbols)

# Global variables
first_card = None
second_card = None
buttons = {}
matches_found = 0

def button_clicked(index):
    global first_card, second_card, matches_found

    if buttons[index]['text'] == '':
        buttons[index]['text'] = symbols[index]
        buttons[index].update_idletasks()

        if first_card is None:
            first_card = index
        elif second_card is None:
            second_card = index
            if symbols[first_card] == symbols[second_card]:
                matches_found += 1
                first_card, second_card = None, None
                if matches_found == len(symbols) // 2:
                    messagebox.showinfo("Game Over", "Congratulations! You've matched all cards!")
            else:
                # Cards do not match; flip back after short delay
                buttons[first_card].after(500, hide_cards, first_card, second_card)

def hide_cards(card1, card2):
    global first_card, second_card
    buttons[card1]['text'] = ''
    buttons[card2]['text'] = ''
    first_card, second_card = None, None

# Create game window
window = tk.Tk()
window.title("Card Matching Game")

# Generate buttons
for i in range(16):
    button = tk.Button(window, text='', width=6, height=3, font=('Arial', 24),
                       command=lambda i=i: button_clicked(i))
    button.grid(row=i // 4, column=i % 4)
    buttons[i] = button

window.mainloop()

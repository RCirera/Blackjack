# This is the main file of the blackjack project

import tkinter as tk
from tkinter import ttk
import time
from definitions import Card, Hand


# Create the player and dealer hands
dealer_hand = Hand()
player_hand = Hand()

# Create the GUI
# Create the root
root = tk.Tk()
root.title("Blackjack (Simplified)")

# Create the static labels
dealer_hand_label = ttk.Label(root, text="Dealer's Hand:", width=12)
dealer_hand_label.grid(row=0, column=0)
dealer_count_label = ttk.Label(root, text="Dealer's Count:", width=12)
dealer_count_label.grid(row=1, column=0)

player_hand_label = ttk.Label(root, text="Player's Hand:", width=12)
player_hand_label.grid(row=2, column=0)
player_count_label = ttk.Label(root, text="Player's Count:", width=12)
player_count_label.grid(row=3, column=0)

# Create the variables
dealer_hand_str = tk.StringVar()
dealer_count_int = tk.IntVar()
dealer_count_int.set(dealer_hand.value)

player_hand_str = tk.StringVar()
player_count_int = tk.IntVar()
player_count_int.set(player_hand.value)

game_state_str = tk.StringVar()
game_state_str.set("Click \'New Game\' to start")

# Create the variable labels
dealer_hand_var_label = ttk.Label(root, textvariable=dealer_hand_str)
dealer_hand_var_label.grid(row=0, column=1)
dealer_count_var_label = ttk.Label(root, textvariable=dealer_count_int)
dealer_count_var_label.grid(row=1, column=1)

player_hand_var_label = ttk.Label(root, textvariable=player_hand_str, anchor="w")
player_hand_var_label.grid(row=2, column=1)
player_count_var_label = ttk.Label(root, textvariable=player_count_int)
player_count_var_label.grid(row=3, column=1)

game_state_var_label = ttk.Label(root, textvariable=game_state_str)
game_state_var_label.grid(row=4, column=0, columnspan=2)

# Define the button functions


def stand():
    hit_button.config(state=tk.DISABLED)
    stand_button.config(state=tk.DISABLED)

    while dealer_hand.value < 17:
        dealer_hand.append(Card())
        dealer_count_int.set(dealer_hand.value)
        dealer_hand_str.set(dealer_hand.card_faces)
        root.update()
        time.sleep(0.5)
    check_game_state()
    return


def hit():
    player_hand.append(Card())
    player_hand_str.set(player_hand.card_faces)
    player_count_int.set(player_hand.value)
    check_player_bust()
    return


def new_game():
    dealer_hand.empty()
    player_hand.empty()
    dealer_hand.append(Card())
    dealer_hand_str.set(dealer_hand.card_faces)
    dealer_count_int.set(dealer_hand.value)

    player_hand.append(Card())
    player_hand_str.set(player_hand.card_faces)
    player_count_int.set(player_hand.value)

    game_state_str.set("Game on")

    hit_button.config(state=tk.NORMAL)
    stand_button.config(state=tk.NORMAL)
    return


# Create the buttons
hit_button = ttk.Button(root, text="Hit", command=hit, state=tk.DISABLED)
hit_button.grid(row=5, column=0)
stand_button = ttk.Button(root, text="Stand", command=stand, state=tk.DISABLED)
stand_button.grid(row=5, column=1)
new_gameButton = ttk.Button(root, text="New Game", command=new_game)
new_gameButton.grid(row=6, column=0)
exit_button = ttk.Button(root, text="Exit", command=quit)
exit_button.grid(row=6, column=1)

# Add some space between the widgets
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)


# Define other functions

def check_player_bust():
    if player_hand.value > 21:
        game_state_str.set("Player Busted! Dealer Wins")
        
        hit_button.config(state=tk.DISABLED)
        stand_button.config(state=tk.DISABLED)


def check_game_state():
    if dealer_hand.value > 21:
        game_state_str.set("Dealer Busted! Player Wins!")
    elif player_hand.value > dealer_hand.value:
        game_state_str.set("Player Wins!")
    elif player_hand.value == dealer_hand.value:
        game_state_str.set("Tie!")
    else:
        game_state_str.set("Dealer Wins!")


# Activate GUI loop
root.mainloop()

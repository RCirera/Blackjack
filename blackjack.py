# This is the main file of the blackjack project

import tkinter as tk
from tkinter import ttk
import time
import random


# Create the GUI

# Create the root
root = tk.Tk()
root.title("Blackjack (Simplified)")

# Create the static labels
dealerHandLabel = ttk.Label(root, text="Dealer's Hand:", width=12)
dealerHandLabel.grid(row=0, column=0)
dealerCountLabel = ttk.Label(root, text="Dealer's Count:", width=12)
dealerCountLabel.grid(row=1, column=0)
playerHandLabel = ttk.Label(root, text="Player's Hand:", width=12)
playerHandLabel.grid(row=2, column=0)
playerCountLabel = ttk.Label(root, text="Player's Count:", width=12)
playerCountLabel.grid(row=3, column=0)

# Create the variables
dealerCountInt = tk.IntVar()
dealerCountInt.set(0)
playerCountInt = tk.IntVar()
playerCountInt.set(0)
gameStateStr = tk.StringVar()
gameStateStr.set("Click \'New Game\' to start")

playerHandStr = tk.StringVar()
dealerHandStr = tk.StringVar()

# Create the variable labels
dealerCountVarLabel = ttk.Label(root, textvariable=dealerCountInt)
dealerCountVarLabel.grid(row=1, column=1)
playerCountVarLabel = ttk.Label(root, textvariable=playerCountInt)
playerCountVarLabel.grid(row=3, column=1)
gameStateVarLabel = ttk.Label(root, textvariable=gameStateStr)
gameStateVarLabel.grid(row=4, column=0, columnspan=2)

playerHandVarLabel = ttk.Label(root, textvariable=playerHandStr, anchor="w")
playerHandVarLabel.grid(row=2, column=1)
dealerHandVarLabel = ttk.Label(root, textvariable=dealerHandStr)
dealerHandVarLabel.grid(row=0, column=1)

# Define the button functions


def stand():
    while dealerCountInt.get() < 17:
        dealerCardInt = deal()
        dealerCardStr = str(dealerCardInt)
        dealerCountInt.set(dealerCountInt.get()+dealerCardInt)
        dealerHandStr.set(dealerHandStr.get() + ", " + dealerCardStr)
        root.update()
        time.sleep(0.5)
    checkGameState()
    return


def hit():
    cardInt = deal()
    cardStr = str(cardInt)
    playerCountInt.set(playerCountInt.get()+cardInt)
    playerHandStr.set(playerHandStr.get()+", "+cardStr)
    checkPlayerBust()
    return


def newGame():
    playerCardInt = deal()
    playerCardStr = str(playerCardInt)
    dealerCardInt = deal()
    dealerCardStr = str(dealerCardInt)

    dealerCountInt.set(dealerCardInt)
    dealerHandStr.set(dealerCardStr)
    playerCountInt.set(playerCardInt)
    playerHandStr.set(playerCardStr)
    gameStateStr.set("Game on")
    hitButton.config(state=tk.NORMAL)
    standButton.config(state=tk.NORMAL)
    return


# Create the buttons
hitButton = ttk.Button(root, text="Hit", command=hit, state=tk.DISABLED)
hitButton.grid(row=5, column=0)
standButton = ttk.Button(root, text="Stand", command=stand, state=tk.DISABLED)
standButton.grid(row=5, column=1)
newGameButton = ttk.Button(root, text="New Game", command=newGame)
newGameButton.grid(row=6, column=0)
exitButton = ttk.Button(root, text="Exit", command=quit)
exitButton.grid(row=6, column=1)

# Add some space between the widgets
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)


# Define other functions

def checkPlayerBust():
    if playerCountInt.get() > 21:
        gameStateStr.set("Player Bust, Dealer Wins")
        hitButton.config(state=tk.DISABLED)
        standButton.config(state=tk.DISABLED)


def checkGameState():
    hitButton.config(state=tk.DISABLED)
    standButton.config(state=tk.DISABLED)
    if dealerCountInt.get() > 21:
        gameStateStr.set("Dealer Bust! Player Wins!")
    elif playerCountInt.get() > dealerCountInt.get():
        gameStateStr.set("Player Wins!")
    elif playerCountInt.get() == dealerCountInt.get():
        gameStateStr.set("Tie!")
    else:
        gameStateStr.set("Dealer Wins!")


def deal():
    card = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    return card


# Activate GUI loop
root.mainloop()
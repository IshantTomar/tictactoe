import random
from customtkinter import *

window = CTk()
window.title("TicTacToe")
set_appearance_mode("dark")

symbols = ["O", "X"]
player = random.choice(symbols)
board = [["0", "1", "2"],
         ["3", "4", "5"],
         ["6", "7", "8"]]

def checkwin(player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw():
    return all(cell in ["O", "X"] for row in board for cell in row)

def play(button, row, col):
    global player
    if button.cget("text") == "":
        button.configure(text=player)
        board[row][col] = player
        if checkwin(player):
            info_label.configure(text=f"{player} won")
            disable_buttons()
        elif check_draw():
            info_label.configure(text="It's a draw!")
        else:
            player = "O" if player == "X" else "X"
            info_label.configure(text=f"{player}'s turn")

def disable_buttons():
    for row in buttons:
        for button in row:
            button.configure(state="disabled")

def reset_game():
    global player, board
    player = random.choice(symbols)
    board = [["0", "1", "2"],
             ["3", "4", "5"],
             ["6", "7", "8"]]
    info_label.configure(text=f"{player}'s turn")
    for row in buttons:
        for button in row:
            button.configure(text="", state="normal")

info_label = CTkLabel(window, text=f"{player}'s turn", font=("Arial", 50))
info_label.grid(row=0, columnspan=3, pady=20)

buttons = []

for r in range(3):  # Loop over rows
    button_row = []
    for c in range(3):  # Loop over columns
        button = CTkButton(window, text="", height=80, width=80, font=("Arial", 70))
        button.configure(command=lambda b=button, row=r, col=c: play(b, row, col))
        button.grid(row=r + 1, column=c, padx=3, pady=3)
        button_row.append(button)
    buttons.append(button_row)

reset_button = CTkButton(window, text="Reset", width=20,font=("Arial", 20), fg_color="#079c02", hover_color="#034a01", command=reset_game)
reset_button.grid(row=4, columnspan=3, pady=5)

window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=0)
window.grid_rowconfigure(2, weight=0)
window.grid_rowconfigure(3, weight=0)
window.grid_rowconfigure(4, weight=0)
window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=0)
window.grid_columnconfigure(2, weight=0)
window.grid_columnconfigure(3, weight=0)
window.grid_columnconfigure(4, weight=0)
window.mainloop()

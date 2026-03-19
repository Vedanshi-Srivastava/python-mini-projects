'''import random
cscore = 0
hscore = 0
while True:
    print(f"Current Score: Your Score = {hscore}, Computer Score = {cscore}\n")
    user = int(input("1 for Stone, 2 for Paper, 3 for Scissors.\n Choose one :- "))
    com = random.randint(1,3)
    if user ==1 and com ==3:
        hscore+=1
        print("You won this round!")
    elif user == 2 and com == 1:
        hscore+=1
        print("You won this round!")
    elif user == 3 and com == 2:
        hscore+=1
        print("You won this round!")
    elif user == com:
        print("It was a draw")
    else:
        cscore +=1
        print("Computer won this round!")
    if cscore == 5:
        print(" OOPS! Computer won this game! \n Better luck next time")
        break
    elif hscore == 5:
        print("Woohoo!! Congratulations! \nYou won this game!")
        break'''
import tkinter as tk
import random

# Game variables
hscore = 0
cscore = 0

choices = {1: "Stone", 2: "Paper", 3: "Scissors"}

def play(user_choice):
    global hscore, cscore

    com_choice = random.randint(1, 3)
    com_choice_label.config(text=f"Computer chose: {choices[com_choice]}")

    # Game logic
    if user_choice == com_choice:
        result_label.config(text="It's a Draw!", fg="orange")

    elif (user_choice == 1 and com_choice == 3) or \
         (user_choice == 2 and com_choice == 1) or \
         (user_choice == 3 and com_choice == 2):
        hscore += 1
        result_label.config(text="You Won This Round!", fg="green")
    else:
        cscore += 1
        result_label.config(text="Computer Won This Round!", fg="red")

    # Update scores
    score_label.config(text=f"Your Score: {hscore}    Computer Score: {cscore}")

    # Check win condition
    if hscore == 5:
        result_label.config(text="🎉 YOU WON THE GAME!", fg="green")
        disable_buttons()
    elif cscore == 5:
        result_label.config(text="❌ COMPUTER WON THE GAME!", fg="red")
        disable_buttons()

def disable_buttons():
    stone_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")

def restart_game():
    global hscore, cscore
    hscore = 0
    cscore = 0
    score_label.config(text=f"Your Score: {hscore}    Computer Score: {cscore}")
    result_label.config(text="Make your move!")
    com_choice_label.config(text="Computer chose: ---")

    stone_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissors_btn.config(state="normal")

# UI Window
root = tk.Tk()
root.title("Stone Paper Scissors")
root.geometry("420x350")
root.config(bg="#f4f4f4")

title_label = tk.Label(root, text="🪨📄✂ Stone–Paper–Scissors", font=("Arial", 16, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0    Computer Score: 0",
                       font=("Arial", 14), bg="#f4f4f4")
score_label.pack(pady=5)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 14), bg="#f4f4f4")
result_label.pack(pady=10)

com_choice_label = tk.Label(root, text="Computer chose: ---", font=("Arial", 12), bg="#f4f4f4")
com_choice_label.pack(pady=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f4f4f4")
btn_frame.pack(pady=20)

stone_btn = tk.Button(btn_frame, text="🪨 Stone", font=("Arial", 12),
                      width=10, command=lambda: play(1))
stone_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(btn_frame, text="📄 Paper", font=("Arial", 12),
                      width=10, command=lambda: play(2))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(btn_frame, text="✂ Scissors", font=("Arial", 12),
                         width=10, command=lambda: play(3))
scissors_btn.grid(row=0, column=2, padx=10)

restart_btn = tk.Button(root, text="🔄 Restart Game", font=("Arial", 12),
                        command=restart_game, bg="#2196F3", fg="white")
restart_btn.pack(pady=10)

root.mainloop()

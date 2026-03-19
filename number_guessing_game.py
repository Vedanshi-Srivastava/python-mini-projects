'''import random
num = random.randint(1,100)
tries = 0
while True:
    guessed = int(input("Guess the number between 1 to 100 :"))
    tries +=1
    if guessed == num:
        print(f"Congratulations you found your number in {tries} tries")
        break
    elif guessed > num:
        print("Sorry you need to go lower")
    elif guessed<num:
        print("Sorry you have to go upper")'''
import tkinter as tk
import random

# Generate the random number
num = random.randint(1, 100)
tries = 0

def check_guess():
    global tries, num
    guess = guess_entry.get()

    if not guess.isdigit(): 
        result_label.config(text="Please enter a valid number!")
        return

    guess = int(guess)
    tries += 1

    if guess == num:
        result_label.config(text=f"🎉 Correct! You found it in {tries} tries!")
    elif guess > num:
        result_label.config(text="🔻 Go Lower!")
    else:
        result_label.config(text="🔺 Go Higher!")

def restart_game():
    global num, tries
    num = random.randint(1, 100)
    tries = 0
    guess_entry.delete(0, tk.END)
    result_label.config(text="New Game Started! Guess a number 1–100.")

# Main Window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x250")
root.config(bg="#f4f4f4")

# Heading
title_label = tk.Label(root, text="🎯 Number Guessing Game", font=("Arial", 16, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

# Input Entry
guess_entry = tk.Entry(root, font=("Arial", 14), width=10, justify="center")
guess_entry.pack()

# Guess Button
guess_button = tk.Button(root, text="Guess", font=("Arial", 12), command=check_guess, bg="#4CAF50", fg="white")
guess_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Guess a number between 1 and 100!", font=("Arial", 12), bg="#f4f4f4")
result_label.pack(pady=10)

# Restart Button
restart_button = tk.Button(root, text="Restart Game", font=("Arial", 12), command=restart_game, bg="#2196F3", fg="white")
restart_button.pack()

root.mainloop()

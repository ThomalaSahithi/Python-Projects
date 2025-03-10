import random
import os
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk  # Import Pillow

# Choices and their respective image paths
choices = ["rock", "paper", "scissors"]
image_paths = {
    "rock": "images/rock.png",
    "paper": "images/paper.png",
    "scissors": "images/scissors.png"
}

# Score tracking
player_score = 0
computer_score = 0


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_image(path):
    """Loads an image using Pillow and converts it for Tkinter."""
    img = Image.open(path)
    img = img.resize((100, 100), Image.LANCZOS)  # Resize image if needed
    return ImageTk.PhotoImage(img)


def play(choice):
    global player_score, computer_score
    computer_choice = random.choice(choices)

    if choice == computer_choice:
        result_text.set("It's a Tie!")
    elif (choice == "rock" and computer_choice == "scissors") or \
            (choice == "paper" and computer_choice == "rock") or \
            (choice == "scissors" and computer_choice == "paper"):
        result_text.set("You Win!")
        player_score += 1
    else:
        result_text.set("You Lose!")
        computer_score += 1

    update_score()
    update_images(choice, computer_choice)


def update_score():
    score_text.set(f"Player: {player_score}  Computer: {computer_score}")


def update_images(player_choice, computer_choice):
    player_img = load_image(image_paths[player_choice])
    computer_img = load_image(image_paths[computer_choice])

    player_image.config(image=player_img)
    player_image.image = player_img  # Keep reference
    computer_image.config(image=computer_img)
    computer_image.image = computer_img  # Keep reference


def play_again():
    clear_screen()
    result_text.set("Choose Rock, Paper, or Scissors")
    player_image.config(image=default_image)
    computer_image.config(image=default_image)


def exit_game():
    root.destroy()


# GUI Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x400")

result_text = tk.StringVar()
result_text.set("Choose Rock, Paper, or Scissors")
score_text = tk.StringVar()
score_text.set("Player: 0  Computer: 0")

# Load default image
default_image = load_image("../Hangman Game/images/default.png")

Label(root, textvariable=result_text, font=("Arial", 14)).pack()

frame = tk.Frame(root)
frame.pack()

player_image = Label(frame, image=default_image)
player_image.pack(side=tk.LEFT, padx=20)
computer_image = Label(frame, image=default_image)
computer_image.pack(side=tk.RIGHT, padx=20)

Label(root, textvariable=score_text, font=("Arial", 12)).pack()

button_frame = tk.Frame(root)
button_frame.pack()

for choice in choices:
    Button(button_frame, text=choice.capitalize(), command=lambda ch=choice: play(ch)).pack(side=tk.LEFT, padx=10)

Button(root, text="Play Again", command=play_again).pack()
Button(root, text="Exit", command=exit_game).pack()

root.mainloop()


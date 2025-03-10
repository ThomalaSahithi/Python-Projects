import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def choose_word():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words)

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.word = choose_word()
        self.guessed_letters = set()
        self.attempts = 6
        self.score = 0
        self.highest_score = 0

        self.label_score = tk.Label(root, text=f"Score: {self.score} | Highest Score: {self.highest_score}", font=("Arial", 14))
        self.label_score.pack()

        self.hangman_images = self.load_images()
        self.label_hangman = tk.Label(root, image=self.hangman_images[6 - self.attempts])
        self.label_hangman.pack()

        self.label_word = tk.Label(root, text=self.get_display_word(), font=("Arial", 16))
        self.label_word.pack()

        self.entry_guess = tk.Entry(root)
        self.entry_guess.pack()

        self.button_guess = tk.Button(root, text="Guess", command=self.make_guess)
        self.button_guess.pack()

    def load_images(self):
        images = []
        for i in range(7):  # Load images in reverse order
            path = os.path.join("images", f"hangman{i}.png")
            images.append(ImageTk.PhotoImage(Image.open(path)))
        return images

    def get_display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.word)

    def make_guess(self):
        guess = self.entry_guess.get().lower()
        self.entry_guess.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        if guess not in self.word:
            self.attempts -= 1
        else:
            if all(letter in self.guessed_letters for letter in self.word):
                self.score += 1
                self.highest_score = max(self.score, self.highest_score)
                messagebox.showinfo("Congratulations!", f"You guessed the word: {self.word}")
                self.reset_game()
                return

        self.update_display()
        if self.attempts == 0:
            messagebox.showerror("Game Over", f"The word was: {self.word}")
            self.reset_game(full_reset=True)

    def update_display(self):
        self.label_score.config(text=f"Score: {self.score} | Highest Score: {self.highest_score}")
        self.label_hangman.config(image=self.hangman_images[6 - self.attempts])
        self.label_word.config(text=self.get_display_word())

    def reset_game(self, full_reset=False):
        if full_reset:
            self.score = 0
        self.word = choose_word()
        self.guessed_letters.clear()
        self.attempts = 6
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

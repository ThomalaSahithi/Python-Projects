import tkinter as tk
import random
from tkinter import messagebox

class HigherLowerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Higher-Lower Game")

        self.score = 0
        self.highest_score = 0
        self.current_number = random.randint(1, 100)

        # Score Display
        self.label_score = tk.Label(root, text=f"Score: {self.score} | Highest Score: {self.highest_score}", font=("Arial", 12))
        self.label_score.pack(pady=5)

        # Current Number Display
        self.label_number = tk.Label(root, text=f"Current Number: {self.current_number}", font=("Arial", 18, "bold"))
        self.label_number.pack(pady=10)

        # Buttons for Higher and Lower
        self.button_higher = tk.Button(root, text="Higher", font=("Arial", 14), command=lambda: self.check_guess("higher"))
        self.button_higher.pack(side="left", padx=20, pady=10)

        self.button_lower = tk.Button(root, text="Lower", font=("Arial", 14), command=lambda: self.check_guess("lower"))
        self.button_lower.pack(side="right", padx=20, pady=10)

    def check_guess(self, guess):
        next_number = random.randint(1, 100)
        correct_guess = (guess == "higher" and next_number > self.current_number) or (guess == "lower" and next_number < self.current_number)

        if correct_guess:
            self.score += 1
            self.highest_score = max(self.score, self.highest_score)
            self.current_number = next_number
            self.label_number.config(text=f"Current Number: {self.current_number}")
            self.label_score.config(text=f"Score: {self.score} | Highest Score: {self.highest_score}")
        else:
            messagebox.showerror("Game Over", f"Wrong! The next number was {next_number}.")
            self.ask_play_again()

    def ask_play_again(self):
        play_again = messagebox.askyesno("Game Over", "Do you want to play again?")
        if play_again:
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.score = 0
        self.current_number = random.randint(1, 100)
        self.label_number.config(text=f"Current Number: {self.current_number}")
        self.label_score.config(text=f"Score: {self.score} | Highest Score: {self.highest_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = HigherLowerGame(root)
    root.mainloop()

import tkinter as tk
import random
from tkinter import messagebox


class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")

        self.highest_score = 0
        self.score = 0  # Initialize score at the beginning

        # Score Label
        self.label_score = tk.Label(root, text=f"Score: {self.score} | Highest Score: {self.highest_score}",
                                    font=("Arial", 12))
        self.label_score.pack(pady=5)

        # Instruction Label
        self.label = tk.Label(root, text="Guess a number between 1 and 100:", font=("Arial", 14))
        self.label.pack(pady=10)

        # Entry Field
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit Guess", font=("Arial", 14), command=self.check_guess)
        self.submit_button.pack(pady=5)

        # Result Label (Now Defined Before reset_game is Called)
        self.result_label = tk.Label(root, text="Attempts left: 6", font=("Arial", 14))
        self.result_label.pack(pady=5)

        # Now Reset the Game (Since result_label Exists)
        self.reset_game()

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.entry.delete(0, tk.END)

            if user_guess < 1 or user_guess > 100:
                self.result_label.config(text="Out of range! Enter 1-100.", fg="red")
                return

            self.attempts -= 1

            if user_guess < self.target_number:
                self.result_label.config(text=f"Too Low! Attempts left: {self.attempts}", fg="blue")
            elif user_guess > self.target_number:
                self.result_label.config(text=f"Too High! Attempts left: {self.attempts}", fg="blue")
            else:
                self.result_label.config(text=f"🎉 Correct! You won.", fg="green")
                self.score += 1
                self.highest_score = max(self.score, self.highest_score)
                self.ask_continue()
                return

            if self.attempts == 0:
                messagebox.showerror("Game Over", f"The number was {self.target_number}.")
                self.score = 0
                self.ask_play_again()

        except ValueError:
            self.result_label.config(text="Invalid input! Enter a number.", fg="red")

        self.label_score.config(text=f"Score: {self.score} | Highest Score: {self.highest_score}")

    def ask_continue(self):
        play = messagebox.askyesno("You Won!", "Do you want to continue?")
        if play:
            self.reset_game()
        else:
            self.root.quit()

    def ask_play_again(self):
        play = messagebox.askyesno("Game Over", "Do you want to play again?")
        if play:
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 10
        self.result_label.config(text=f"Attempts left: {self.attempts}", fg="black")
        self.label_score.config(text=f"Score: {self.score} | Highest Score: {self.highest_score}")


# Run the GUI Application
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()

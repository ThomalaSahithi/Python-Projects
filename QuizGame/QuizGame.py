import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import random
import time
import pygame
import os

# Initialize pygame mixer for sound
pygame.mixer.init()
correct_sound_path = "sounds/correct.wav"
wrong_sound_path = "sounds/wrong.wav"

# Load sound files
correct_sound = pygame.mixer.Sound(correct_sound_path) if os.path.exists(correct_sound_path) else None
wrong_sound = pygame.mixer.Sound(wrong_sound_path) if os.path.exists(wrong_sound_path) else None


# Load questions from JSON
def load_questions():
    with open("data/questions.json", "r") as file:
        return json.load(file)


# Quiz Game class
class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 Quiz Game")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f4ff")  # Light pastel blue background
        self.questions = load_questions()
        self.score = 0
        self.current_question_index = 0
        self.start_time = time.time()
        self.selected_category = "Technology"
        self.selected_difficulty = "Easy"
        self.leaderboard_file = "leaderboard.json"
        self.timer_running = False

        self.load_leaderboard()
        self.create_ui()

    def create_ui(self):
        # Title Label
        tk.Label(self.root, text="📚 Quiz Game", font=("Arial", 20, "bold"), bg="#f0f4ff", fg="#333").pack(pady=10)

        # Category Selection
        tk.Label(self.root, text="Select Category:", font=("Arial", 14), bg="#f0f4ff").pack()
        self.category_var = tk.StringVar(value=self.selected_category)
        categories = list(self.questions.keys())
        for cat in categories:
            tk.Radiobutton(self.root, text=cat, variable=self.category_var, value=cat, bg="#f0f4ff").pack()

        # Difficulty Selection
        tk.Label(self.root, text="Select Difficulty:", font=("Arial", 14), bg="#f0f4ff").pack()
        self.difficulty_var = tk.StringVar(value=self.selected_difficulty)
        difficulties = ["Easy", "Medium", "Hard"]
        for diff in difficulties:
            tk.Radiobutton(self.root, text=diff, variable=self.difficulty_var, value=diff, bg="#f0f4ff").pack()

        # Start Button
        tk.Button(self.root, text="Start Quiz", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",
                  command=self.start_quiz, padx=10, pady=5).pack(pady=10)

        # Question Label
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16, "bold"), bg="#f0f4ff", wraplength=400)
        self.question_label.pack(pady=10)

        # Answer Buttons
        self.options_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Arial", 12), bg="#ddd", fg="#333", height=2, width=40,
                            relief="ridge", command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.options_buttons.append(btn)

        # Timer & Score
        self.timer_label = tk.Label(self.root, text="⏳ Time Left: 10s", font=("Arial", 12, "bold"), bg="#f0f4ff",
                                    fg="red")
        self.timer_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="🏆 Score: 0", font=("Arial", 14, "bold"), bg="#f0f4ff", fg="#444")
        self.score_label.pack()

    def start_quiz(self):
        self.selected_category = self.category_var.get()
        self.selected_difficulty = self.difficulty_var.get()
        self.filtered_questions = self.questions[self.selected_category][self.selected_difficulty]

        random.shuffle(self.filtered_questions)
        self.score = 0
        self.current_question_index = 0
        self.ask_question()

    def ask_question(self):
        if self.current_question_index < len(self.filtered_questions):
            self.timer_running = True
            question_data = self.filtered_questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])

            # Shuffle options but keep track of the correct one
            self.correct_answer = question_data["answer"]
            options = question_data["options"]
            random.shuffle(options)

            for i, btn in enumerate(self.options_buttons):
                btn.config(text=options[i], bg="#ddd", fg="#333", state=tk.NORMAL)

            self.start_time = time.time()
            self.update_timer()
        else:
            self.end_quiz()

    def update_timer(self):
        if not self.timer_running:
            return

        elapsed_time = int(time.time() - self.start_time)
        remaining_time = max(10 - elapsed_time, 0)
        self.timer_label.config(text=f"⏳ Time Left: {remaining_time}s")

        if remaining_time > 0:
            self.root.after(1000, self.update_timer)
        else:
            self.check_answer(-1)

    def check_answer(self, selected_index):
        self.timer_running = False
        question_data = self.filtered_questions[self.current_question_index]
        selected_answer = self.options_buttons[selected_index].cget("text") if selected_index != -1 else ""

        if selected_answer == self.correct_answer:
            self.score += 10
            self.options_buttons[selected_index].config(bg="#4CAF50", fg="white")
            if correct_sound:
                correct_sound.play()
        else:
            self.options_buttons[selected_index].config(bg="red", fg="white")
            if wrong_sound:
                wrong_sound.play()

        self.current_question_index += 1
        self.score_label.config(text=f"🏆 Score: {self.score}")
        self.root.after(1000, self.ask_question)  # Pause briefly before next question

    def end_quiz(self):
        messagebox.showinfo("Quiz Over", f"Your final score is: {self.score}")
        self.save_score()
        self.show_leaderboard()

    def save_score(self):
        player_name = simpledialog.askstring("Leaderboard", "Enter your name:")
        if not player_name:
            player_name = "Anonymous"

        self.leaderboard.append({"name": player_name, "score": self.score})
        self.leaderboard.sort(key=lambda x: x["score"], reverse=True)

        with open(self.leaderboard_file, "w") as file:
            json.dump(self.leaderboard[:10], file)

    def load_leaderboard(self):
        if os.path.exists(self.leaderboard_file):
            with open(self.leaderboard_file, "r") as file:
                self.leaderboard = json.load(file)
        else:
            self.leaderboard = []

    def show_leaderboard(self):
        scores_text = "\n".join([f"{entry['name']}: {entry['score']}" for entry in self.leaderboard[:10]])
        messagebox.showinfo("🏆 Leaderboard", scores_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()

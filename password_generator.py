import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password(length=12, use_digits=True, use_special_chars=True):
    """Generates a random password with given length and options."""
    characters = string.ascii_letters  # Includes both uppercase and lowercase letters

    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_and_display():
    try:
        length = int(length_entry.get())
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()

        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters.")
            return

        password = generate_password(length, use_digits, use_special_chars)
        result_var.set(password)
        ask_generate_again()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")


def ask_generate_again():
    response = messagebox.askyesno("Generate Again", "Do you want to generate another password?")
    if response:
        result_var.set("")


# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

tk.Label(root, text="Enter Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

digits_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Digits", variable=digits_var).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var).pack()

tk.Button(root, text="Generate Password", command=generate_and_display).pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Entry(root, textvariable=result_var, state='readonly', width=30)
result_label.pack(pady=5)

tk.Button(root, text="Copy", command=lambda: root.clipboard_append(result_var.get())).pack(pady=5)

tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()

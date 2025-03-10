import tkinter as tk
from tkinter import messagebox


def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def process_text(encrypt=True):
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be a number!")
        return

    result = caesar_cipher(text, shift, encrypt)
    label_result.config(text=f"Result: {result}")


# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher")

tk.Label(root, text="Enter Text:").pack()
entry_text = tk.Entry(root, width=50)
entry_text.pack()

tk.Label(root, text="Enter Shift Value:").pack()
entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

btn_encrypt = tk.Button(root, text="Encrypt", command=lambda: process_text(True))
btn_encrypt.pack()

btn_decrypt = tk.Button(root, text="Decrypt", command=lambda: process_text(False))
btn_decrypt.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

root.mainloop()

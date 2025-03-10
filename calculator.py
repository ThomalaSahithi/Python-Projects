import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry field to display calculations
        self.expression = ""
        self.entry_var = tk.StringVar()
        self.entry_field = tk.Entry(root, textvariable=self.entry_var, font=("Arial", 18), justify="right", bd=10, relief="ridge")
        self.entry_field.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

        # Buttons Layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)
        ]

        # Create buttons dynamically
        for btn in buttons:
            text, row, col = btn[:3]
            colspan = btn[3] if len(btn) == 4 else 1
            self.create_button(text, row, col, colspan)

    def create_button(self, text, row, col, colspan=1):
        button = tk.Button(self.root, text=text, font=("Arial", 18), width=5, height=2,
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = eval(self.expression)  # Evaluate the expression
                self.entry_var.set(result)
                self.expression = str(result)
            except Exception:
                self.entry_var.set("Error")
                self.expression = ""
        elif button_text == "C":
            self.expression = ""
            self.entry_var.set("")
        else:
            self.expression += button_text
            self.entry_var.set(self.expression)

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

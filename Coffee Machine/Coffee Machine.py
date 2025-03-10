import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pygame
import os

# Initialize pygame mixer for sound
pygame.mixer.init()

# Load sound
sound_path = "serve.wav"  # Place this file in the same folder
if os.path.exists(sound_path):
    serve_sound = pygame.mixer.Sound(sound_path)
else:
    serve_sound = None
    print("Error: Sound file not found - serve.wav")


# Coffee Machine Class
class CoffeeMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("☕ Coffee Machine ☕")
        self.root.geometry("500x700")
        self.root.configure(bg="#6F4E37")  # Coffee brown background

        self.balance = 0
        self.earnings = 0
        self.resources = {"water": 500, "milk": 500, "coffee": 100}

        self.menu = {
            "Espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 15, "image": "espresso.png"},
            "Latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 20, "image": "latte.png"},
            "Cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 25, "image": "cappuccino.png"},
        }

        self.create_ui()

    def create_ui(self):
        """Creates the UI Layout."""
        title_label = tk.Label(self.root, text="Welcome to the Coffee Machine!",
                               font=("Arial", 18, "bold"), fg="white", bg="#6F4E37")
        title_label.pack(pady=10)

        # Coffee Selection
        self.coffee_frame = tk.Frame(self.root, bg="#6F4E37")
        self.coffee_frame.pack(pady=10)

        for coffee, details in self.menu.items():
            btn = ttk.Button(self.coffee_frame, text=f"{coffee} (₹{details['cost']})",
                             command=lambda c=coffee: self.process_order(c))
            btn.pack(pady=5, ipadx=20, ipady=5, fill="x")

        # Coin Insert Section
        coin_frame = tk.LabelFrame(self.root, text="💰 Insert Coins", bg="#6F4E37", fg="white",
                                   font=("Arial", 12, "bold"))
        coin_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(coin_frame, text="₹5 Coins:", font=("Arial", 12), fg="white", bg="#6F4E37").grid(row=0, column=0,
                                                                                                  padx=10, pady=5)
        self.coin_5 = ttk.Entry(coin_frame, width=5)
        self.coin_5.grid(row=0, column=1, padx=10)

        tk.Label(coin_frame, text="₹10 Coins:", font=("Arial", 12), fg="white", bg="#6F4E37").grid(row=1, column=0,
                                                                                                   padx=10, pady=5)
        self.coin_10 = ttk.Entry(coin_frame, width=5)
        self.coin_10.grid(row=1, column=1, padx=10)

        tk.Label(coin_frame, text="₹20 Coins:", font=("Arial", 12), fg="white", bg="#6F4E37").grid(row=2, column=0,
                                                                                                   padx=10, pady=5)
        self.coin_20 = ttk.Entry(coin_frame, width=5)
        self.coin_20.grid(row=2, column=1, padx=10)

        # Buttons Section
        btn_frame = tk.Frame(self.root, bg="#6F4E37")
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="🔄 Check Resources", command=self.show_resources).pack(pady=5, fill="x", padx=20)
        ttk.Button(btn_frame, text="⚡ Refill Resources", command=self.refill_resources).pack(pady=5, fill="x", padx=20)
        ttk.Button(btn_frame, text="❌ Exit", command=self.root.quit).pack(pady=5, fill="x", padx=20)

    def process_order(self, coffee):
        """Process the coffee order."""
        details = self.menu[coffee]

        # Check if resources are sufficient
        for item in ["water", "milk", "coffee"]:
            if self.resources[item] < details[item]:
                messagebox.showerror("Error", f"Not enough {item}!")
                return

        # Get money input
        money_inserted = self.get_money()
        if money_inserted < details["cost"]:
            messagebox.showerror("Error", "Not enough money!")
            return

        change = money_inserted - details["cost"]
        self.earnings += details["cost"]

        # Deduct resources
        for item in ["water", "milk", "coffee"]:
            self.resources[item] -= details[item]

        # Serve coffee
        self.display_coffee_image(details["image"])
        if serve_sound:
            serve_sound.play()

        messagebox.showinfo("Enjoy!", f"Here is your {coffee}! ☕\nChange: ₹{change}")

    def get_money(self):
        """Get inserted coins and calculate total money."""
        try:
            five = int(self.coin_5.get() or 0) * 5
            ten = int(self.coin_10.get() or 0) * 10
            twenty = int(self.coin_20.get() or 0) * 20
            return five + ten + twenty
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for coins!")
            return 0

    def display_coffee_image(self, image_name):
        """Display the coffee image when ordered."""
        image_path = image_name
        if os.path.exists(image_path):
            img = Image.open(image_path).resize((150, 150))
            img = ImageTk.PhotoImage(img)
            label = tk.Label(self.root, image=img, bg="#6F4E37")
            label.image = img
            label.pack(pady=10)
        else:
            print(f"Error: Image file not found - {image_path}")

    def show_resources(self):
        """Show available resources and earnings."""
        resources_text = f"💧 Water: {self.resources['water']}ml\n🥛 Milk: {self.resources['milk']}ml\n☕ Coffee: {self.resources['coffee']}g\n💰 Earnings: ₹{self.earnings}"
        messagebox.showinfo("Resources", resources_text)

    def refill_resources(self):
        """Refill resources to default levels."""
        self.resources = {"water": 500, "milk": 500, "coffee": 100}
        messagebox.showinfo("Refilled", "All resources have been refilled!")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    CoffeeMachine(root)
    root.mainloop()

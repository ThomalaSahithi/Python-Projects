import tkinter as tk
from tkinter import messagebox

class SilentAuction:
    def __init__(self, root):
        self.root = root
        self.root.title("Silent Auction")
        self.bids = {}  # Dictionary to store bidder names and their bids

        # Labels
        self.label_title = tk.Label(root, text="Silent Auction", font=("Arial", 18, "bold"))
        self.label_title.pack(pady=10)

        self.label_name = tk.Label(root, text="Enter your Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(root)
        self.entry_name.pack()

        self.label_bid = tk.Label(root, text="Enter your Bid Amount (₹):")
        self.label_bid.pack()
        self.entry_bid = tk.Entry(root)
        self.entry_bid.pack()

        # Buttons
        self.button_submit = tk.Button(root, text="Submit Bid", command=self.submit_bid)
        self.button_submit.pack(pady=5)

        self.button_finish = tk.Button(root, text="Finish Auction", command=self.finish_auction)
        self.button_finish.pack(pady=5)

        self.label_status = tk.Label(root, text="", fg="green", font=("Arial", 12))
        self.label_status.pack()

    def submit_bid(self):
        name = self.entry_name.get().strip()
        bid = self.entry_bid.get().strip()

        if not name or not bid.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid name and numeric bid amount.")
            return

        bid = int(bid)  # Convert bid to integer
        self.bids[name] = bid  # Store bid
        self.label_status.config(text=f"Bid placed successfully by {name}!", fg="blue")

        # Clear input fields
        self.entry_name.delete(0, tk.END)
        self.entry_bid.delete(0, tk.END)

    def finish_auction(self):
        if not self.bids:
            messagebox.showerror("No Bids", "No bids have been placed yet.")
            return

        highest_bidder = max(self.bids, key=self.bids.get)
        highest_bid = self.bids[highest_bidder]

        messagebox.showinfo("Auction Winner", f"🏆 Winner: {highest_bidder} with ₹{highest_bid}!")
        self.root.quit()  # Exit the program after showing results

# Run the Tkinter GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SilentAuction(root)
    root.mainloop()

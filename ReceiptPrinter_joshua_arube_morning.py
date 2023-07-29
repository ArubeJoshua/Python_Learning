import tkinter as tk
from tkinter import messagebox


class ReceiptPrinterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Receipt Printer")

        # Configure padding
        self.root.configure(padx=30, pady=30)

        # Create labels and entry fields
        tk.Label(root, text="Item Name:").grid(row=0, column=0, sticky=tk.W)
        self.item_name_entry = tk.Entry(root)
        self.item_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Price:").grid(row=1, column=0, sticky=tk.W)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create buttons
        tk.Button(root, text="Add Item to receipt", command=self.add_item).grid(
            row=2, column=0, pady=10
        )
        tk.Button(root, text="Print Receipt", command=self.print_receipt).grid(
            row=2, column=1, pady=10
        )

        # Create a text widget for displaying the receipt
        self.receipt_text = tk.Text(root, width=40, height=10)
        self.receipt_text.grid(row=3, columnspan=2)

        tk.Button(root, text="Clear Receipt", command=self.clear_receipt).grid(
            row=4, pady=10
        )

        self.items = []

    def add_item(self):
        item_name = self.item_name_entry.get()
        price = self.price_entry.get()
        if item_name and price:
            try:
                price = float(price)
                self.items.append((item_name, price))
                self.item_name_entry.delete(0, tk.END)
                self.price_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "Item added successfully.")
            except ValueError:
                self.item_name_entry.delete(0, tk.END)
                self.price_entry.delete(0, tk.END)
                messagebox.showerror("Wrong input", "Please enter a valid price.")
        else:
            messagebox.showerror("Error", "Please enter item name and price.")

    def print_receipt(self):
        self.receipt_text.delete(1.0, tk.END)

        total = 0
        self.receipt_text.insert(tk.END, "Receipt\n\n")
        for item_name, price in self.items:
            self.receipt_text.insert(tk.END, f"{item_name}: shs{price}\n")
            total += float(price)

        self.receipt_text.insert(tk.END, f"\nTotal: shs{total:.2f}")
        self.items = []

    def clear_receipt(self):
        self.receipt_text.delete(1.0, tk.END)
        self.items = []


# Create the GUI window
root = tk.Tk()
root.geometry("390x400")
root.configure(background="#F0F0F0")
receipt_printer = ReceiptPrinterGUI(root)

# Run the GUI event loop
root.mainloop()

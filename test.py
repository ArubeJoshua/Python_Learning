import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Beautiful Window")
window.geometry("400x300")

# Customize the window appearance
window.configure(bg="#f1f1f1")  # Set a light gray background color

# Create a styled label with custom font and color
label_title = ttk.Label(
    window, text="Welcome to My App", font=("Arial", 18, "bold"), foreground="blue"
)
label_title.pack(pady=20)

# Create input fields with improved styling
style = ttk.Style()
style.configure(
    "TEntry", padding=5, font=("Arial", 12)
)  # Set padding and font for all Entry widgets

entry_name = ttk.Entry(window)
entry_name.pack(pady=5)

entry_email = ttk.Entry(window)
entry_email.pack(pady=5)

# Create a styled submit button
style.configure(
    "TButton", font=("Arial", 12, "bold"), foreground="white", background="blue"
)
btn_submit = ttk.Button(window, text="Submit")
btn_submit.pack(pady=10)

# Run the main event loop
window.mainloop()

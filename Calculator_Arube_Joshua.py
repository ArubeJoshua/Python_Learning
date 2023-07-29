import tkinter as tk
from tkinter import ttk


# Function to perform the calculation
def calculate():
    try:
        num1 = float(input_1.get())
        num2 = float(input_2.get())
        operator = input_operator.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        label_result.config(text="Result: " + str(result), foreground="black")

    except ValueError:
        label_result.config(text="Invalid input!", foreground="red")


# function to clear fields
def clear():
    input_1.delete(0, tk.END)
    input_2.delete(0, tk.END)
    input_operator.delete(0, tk.END)


# Create the main window
calc_window = tk.Tk()
calc_window.title("Arube Joshua Simple Calculator ")
calc_window.geometry("600x400")
calc_window.configure(bg="#f1f1f1")

# Label
calc_name = ttk.Label(
    calc_window,
    text="J's Simple Calculator",
    font=("Arial", 18, "bold"),
    foreground="blue",
)
calc_name.pack(pady=20)

# Create input fields and labels
style = ttk.Style()
style.configure(
    "TEntry", padding=5, font=("Arial", 12)
)  # Set padding and font for all Entry widgets

label_num1 = ttk.Label(calc_window, text="Number 1:")
label_num1.pack(pady=3)
input_1 = ttk.Entry(calc_window)
input_1.pack()

label_operator = ttk.Label(calc_window, text="Operator (+, -, *, /):")
label_operator.pack(pady=3)
input_operator = ttk.Entry(calc_window)
input_operator.pack()

label_num2 = ttk.Label(calc_window, text="Number 2:")
label_num2.pack(pady=3)
input_2 = ttk.Entry(calc_window)
input_2.pack()

# style buttons
style.configure("TButton", font=("Arial", 12, "bold"), foreground="blue")

frame_buttons = ttk.Frame(calc_window)
frame_buttons.pack()

# Create the calculate button
btn_calculate = ttk.Button(calc_window, text="Calculate", command=calculate)
btn_calculate.grid(row=0, column=0, padx=10, pady=10, in_=frame_buttons)


# Create a clear button
btn_clear = ttk.Button(calc_window, text="Clear", command=clear)
btn_clear.grid(row=0, column=1, padx=10, pady=10, in_=frame_buttons)


# Create a label to display the result
label_result = ttk.Label(calc_window, text="")
label_result.pack(pady=3)

# Run the main event loop
calc_window.mainloop()

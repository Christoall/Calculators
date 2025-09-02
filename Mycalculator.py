#this will be a mini calculator in python lingo

import tkinter as tk

# --- Store history in an array (list) ---
history = []

# --- Functions with parameters ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

# --- Perform calculation and update interface ---
def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            result = "Invalid"

        # Show result
        result_label.config(text=f"Result: {result}")

        # Save to history array
        history.append(result)
        update_history()

    except ValueError:
        result_label.config(text="Please enter valid numbers")

# --- Update history display ---
def update_history():
    history_text.delete(1.0, tk.END)
    for i, res in enumerate(history, start=1):
        history_text.insert(tk.END, f"{i}: {res}\n")

# --- GUI Setup ---
root = tk.Tk()
root.title("Python Calculator")

# Input fields
entry1 = tk.Entry(root, width=45)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=1, padx=10, pady=10)

# Buttons interface
tk.Button(root, text="+", command=lambda: calculate("add")).grid(row=1, column=0)
tk.Button(root, text="-", command=lambda: calculate("subtract")).grid(row=1, column=1)
tk.Button(root, text="×", command=lambda: calculate("multiply")).grid(row=2, column=0)
tk.Button(root, text="÷", command=lambda: calculate("divide")).grid(row=2, column=1)
tk.Button(root, text="Clear History", command=lambda: history.clear() or update_history()).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(root, text="Exit", command=root.quit).grid(row=7, column=0, columnspan=2, pady=5)
tk.Button(root, text="Help", command=lambda: result_label.config(text="Enter numbers and choose an operation")).grid(row=8, column=0, columnspan=2, pady=5)
tk.Button(root, text="delete last", command=lambda: history.pop() if history else None or update_history()).grid(row=9, column=0, columnspan=2, pady=5)
tk.Button(root, text="equals", command=lambda: result_label.config(text=f"Result: {history[-1] if history else 'No history'}")).grid(row=10, column=0, columnspan=2, pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# History area
tk.Label(root, text="History:").grid(row=4, column=0, columnspan=2)
history_text = tk.Text(root, height=5, width=20)
history_text.grid(row=5, column=0, columnspan=2)

root.mainloop()

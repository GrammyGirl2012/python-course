import tkinter as tk

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Multiply Two Numbers")

# Labels and entries for input
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Button to perform multiplication
multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.pack()

# Label to show result
result_label = tk.Label(root, text="Product: ")
result_label.pack()

# Run the application
root.mainloop()

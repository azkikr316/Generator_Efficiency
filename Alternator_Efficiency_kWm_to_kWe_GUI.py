import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def update_labels(event=None):
    option = calculation_choice.get()
    if option == "Calculate kWe (Electrical Output)":
        label_input1.config(text="Mechanical Input (kWm):")
        label_input2.config(text="Efficiency (%):")
    elif option == "Calculate kWm (Mechanical Input)":
        label_input1.config(text="Electrical Output (kWe):")
        label_input2.config(text="Efficiency (%):")
    elif option == "Calculate Efficiency (%)":
        label_input1.config(text="Electrical Output (kWe):")
        label_input2.config(text="Mechanical Input (kWm):")


def calculate():
    try:
        option = calculation_choice.get()
        val1 = float(entry_input1.get())
        val2 = float(entry_input2.get())

        if option == "Calculate kWe (Electrical Output)":
            kwe = val1 * (val2 / 100)
            result.set(f"Result: {kwe:.2f} kWe")
        elif option == "Calculate kWm (Mechanical Input)":
            kwm = val1 / (val2 / 100)
            result.set(f"Result: {kwm:.2f} kWm")
        elif option == "Calculate Efficiency (%)":
            eff = (val1 / val2) * 100
            result.set(f"Result: {eff:.2f}%")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


# Main window
root = tk.Tk()
root.title("Generator Efficiency Calculator")
root.geometry("400x300")
root.resizable(False, False)

# Dropdown for selection
calculation_choice = tk.StringVar(value="Calculate kWe (Electrical Output)")
options = [
    "Calculate kWe (Electrical Output)",
    "Calculate kWm (Mechanical Input)",
    "Calculate Efficiency (%)"
]
ttk.Label(root, text="Select Calculation:").pack(pady=5)
dropdown = ttk.Combobox(root, textvariable=calculation_choice, values=options, state="readonly")
dropdown.pack(pady=5)
dropdown.bind("<<ComboboxSelected>>", update_labels)

# Input fields with dynamic labels
label_input1 = ttk.Label(root, text="Mechanical Input (kWm):")
label_input1.pack(pady=5)
entry_input1 = ttk.Entry(root)
entry_input1.pack(pady=5)

label_input2 = ttk.Label(root, text="Efficiency (%):")
label_input2.pack(pady=5)
entry_input2 = ttk.Entry(root)
entry_input2.pack(pady=5)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=15)

# Result label
result = tk.StringVar()
result_label = ttk.Label(root, textvariable=result, font=("Arial", 12))
result_label.pack(pady=10)

# Initialize labels
update_labels()

# Start GUI loop
root.mainloop()
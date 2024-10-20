import tkinter as tk
from tkinter import ttk
from datetime import date

def calculate_age():
    try:
        birth_year = int(birth_year_entry.get())
        birth_month = int(birth_month_entry.get())
        birth_day = int(birth_day_entry.get())

        today = date.today()
        birth_date = date(birth_year, birth_month, birth_day)

        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        result_label.config(text=f"Your age is: {age}")

    except ValueError:
        result_label.config(text="Please enter valid dates.")

# Create main window
root = tk.Tk()
root.title("Age Calculator")

# Create labels and entry fields
birth_year_label = tk.Label(root, text="Birth Year:")
birth_year_label.grid(row=0, column=0, padx=5, pady=5)
birth_year_entry = tk.Entry(root)
birth_year_entry.grid(row=0, column=1, padx=5, pady=5)

birth_month_label = tk.Label(root, text="Birth Month:")
birth_month_label.grid(row=1, column=0, padx=5, pady=5)
birth_month_entry = tk.Entry(root)
birth_month_entry.grid(row=1, column=1, padx=5, pady=5)

birth_day_label = tk.Label(root, text="Birth Day:")
birth_day_label.grid(row=2, column=0, padx=5, pady=5)
birth_day_entry = tk.Entry(root)
birth_day_entry.grid(row=2, column=1, padx=5, pady=5)

# Create calculate button
calculate_button = ttk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()

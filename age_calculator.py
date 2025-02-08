import tkinter as tk
from tkinter import ttk
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_age():
    try:
        name = name_entry.get().strip()
        birthdate = datetime.strptime(birthdate_entry.get(), "%Y-%m-%d")
        future_date = datetime.strptime(future_date_entry.get(), "%Y-%m-%d")
        age = relativedelta(future_date, birthdate)
        
        # Construct the output message based on non-zero values
        age_str = f"{age.years} years"
        if age.months > 0:
            age_str += f", {age.months} months"
        if age.days > 0:
            age_str += f", and {age.days} days"
        
        if future_date.date() == datetime.now().date():
            result_label.config(text=f"Hey, {name}! Your age today is {age_str}.")
        else:
            result_label.config(text=f"Hey, {name}! Your age on {future_date_entry.get()} will be {age_str}.")
    except ValueError:
        result_label.config(text="Please enter valid dates in YYYY-MM-DD format.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Name entry
ttk.Label(root, text="Enter Your Name:", anchor="w").grid(column=0, row=0, padx=10, pady=5, sticky="w")
name_entry = ttk.Entry(root)
name_entry.grid(column=1, row=0, padx=10, pady=5, sticky="ew")

# Birthdate entry
ttk.Label(root, text="Date of Birth (YYYY-MM-DD):", anchor="w").grid(column=0, row=1, padx=10, pady=5, sticky="w")
birthdate_entry = ttk.Entry(root)
birthdate_entry.grid(column=1, row=1, padx=10, pady=5, sticky="ew")

# Set the current date as the default value for future_date_entry
current_date = datetime.now().strftime("%Y-%m-%d")

# Future date entry
ttk.Label(root, text="Age at the Date of (YYYY-MM-DD):", anchor="w").grid(column=0, row=2, padx=10, pady=5, sticky="w")
future_date_entry = ttk.Entry(root)
future_date_entry.grid(column=1, row=2, padx=10, pady=5, sticky="ew")
future_date_entry.insert(0, current_date)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_age)
calculate_button.grid(column=0, row=3, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=4, columnspan=2, pady=5)

root.grid_columnconfigure(1, weight=1)
root.mainloop()

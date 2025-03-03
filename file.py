import tkinter as tk
from tkinter import ttk

# Conversion factors
conversion_factors = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701,
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e6,
        "Pound": 2.20462,
        "Ounce": 35.274,
    },
    "Temperature": "Special"
}

def convert():
    try:
        category = category_var.get()
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        value = float(entry_value.get())

        if category == "Temperature":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = value + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
        else:
            result = value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
        
        result_label.config(text=f"Result: {result:.4f} {to_unit}")
    except ValueError:
        result_label.config(text="Invalid input")

def update_units(*args):
    category = category_var.get()
    from_unit_menu['menu'].delete(0, 'end')
    to_unit_menu['menu'].delete(0, 'end')
    
    if category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    else:
        units = list(conversion_factors[category].keys())
    
    from_unit_var.set(units[0])
    to_unit_var.set(units[1])
    
    for unit in units:
        from_unit_menu['menu'].add_command(label=unit, command=tk._setit(from_unit_var, unit))
        to_unit_menu['menu'].add_command(label=unit, command=tk._setit(to_unit_var, unit))

# GUI setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

category_var = tk.StringVar()
from_unit_var = tk.StringVar()
to_unit_var = tk.StringVar()
entry_value = tk.StringVar()

category_label = ttk.Label(root, text="Select Category:")
category_label.pack(pady=5)
category_menu = ttk.Combobox(root, textvariable=category_var, values=list(conversion_factors.keys()))
category_menu.pack(pady=5)
category_menu.bind("<<ComboboxSelected>>", update_units)

from_unit_menu = ttk.OptionMenu(root, from_unit_var, "")
from_unit_menu.pack(pady=5)
to_unit_menu = ttk.OptionMenu(root, to_unit_var, "")
to_unit_menu.pack(pady=5)

entry_label = ttk.Label(root, text="Enter Value:")
entry_label.pack(pady=5)
entry = ttk.Entry(root, textvariable=entry_value)
entry.pack(pady=5)

convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

result_label = ttk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()
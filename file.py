import streamlit as st

# Conversion factors
conversion_factors = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701,
    },
    "Weight": {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274,
    },
    "Temperature": "Special"
}

def convert(category, value, from_unit, to_unit):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

# Streamlit UI
st.title("🔢 Unit Converter")

category = st.selectbox("Select Category", list(conversion_factors.keys()))

if category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
else:
    units = list(conversion_factors[category].keys())

from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert(category, value, from_unit, to_unit)
    st.success(f"Converted Value: {result:.4f} {to_unit}")

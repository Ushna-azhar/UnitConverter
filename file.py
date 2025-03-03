import streamlit as st

# 🌟 Set page title and icon
st.set_page_config(page_title="Unit Converter", page_icon="🔢", layout="centered")

# 🎨 Apply custom theme (Blue Gradient)
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #F0F3FA, #638ECB);
            color: #395B86;
        }
        .stApp {
            background: linear-gradient(to right, #F0F3FA, #638ECB);
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #395B86;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stTextInput>div>div>input {
            background-color: #D5DEEF;
            border-radius: 8px;
            padding: 10px;
            color: #395B86;
        }
        .stSelectbox>div {
            background-color: #D5DEEF;
            border-radius: 8px;
            color: #395B86;
        }
        .stSuccess {
            background-color: #B1C9EF;
            padding: 10px;
            border-radius: 8px;
            color: #395B86;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 📏 Available unit categories
unit_categories = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274
    },
    "Temperature": "Special"  # Temperature requires custom conversion
}

# 🔄 Function to handle unit conversion
def convert_units(category, value, from_unit, to_unit):
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
        return value  # No conversion needed
    else:
        return value * (unit_categories[category][to_unit] / unit_categories[category][from_unit])

# 🏷️ Title
st.title("🔢 Unit Converter")

# 📌 Select Category
category = st.selectbox("Select a category", list(unit_categories.keys()))

# 📌 Select Units & Input Value
if category:
    units = list(unit_categories[category].keys())
    from_unit = st.selectbox("Convert from", units)
    to_unit = st.selectbox("Convert to", units)
    value = st.number_input(f"Enter value in {from_unit}", min_value=0.0, format="%.2f")

    # 🔄 Convert Button
    if st.button("Convert"):
        result = convert_units(category, value, from_unit, to_unit)
        st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

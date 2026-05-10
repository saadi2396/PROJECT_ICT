import streamlit as st

# Page setting
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# Main title
st.title("⚙️ Mechanical Unit Converter and Material Density Checker")

# Student information
st.markdown("""
### Student Information
*Full Name:* Muhammad Saad Khan  
*Roll Number:* 25-ME-71
""")

st.divider()

# Unit Converter Section
st.header("🔁 Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Mass", "Force", "Pressure", "Temperature"]
)

value = st.number_input("Enter Value", value=1.0)

if conversion_type == "Length":
    unit = st.selectbox(
        "Select Conversion",
        ["Meter to Feet", "Feet to Meter", "Millimeter to Inch", "Inch to Millimeter"]
    )

    if unit == "Meter to Feet":
        result = value * 3.28084
        output_unit = "ft"
    elif unit == "Feet to Meter":
        result = value / 3.28084
        output_unit = "m"
    elif unit == "Millimeter to Inch":
        result = value / 25.4
        output_unit = "inch"
    else:
        result = value * 25.4
        output_unit = "mm"

elif conversion_type == "Mass":
    unit = st.selectbox(
        "Select Conversion",
        ["Kilogram to Pound", "Pound to Kilogram", "Gram to Kilogram"]
    )

    if unit == "Kilogram to Pound":
        result = value * 2.20462
        output_unit = "lb"
    elif unit == "Pound to Kilogram":
        result = value / 2.20462
        output_unit = "kg"
    else:
        result = value / 1000
        output_unit = "kg"

elif conversion_type == "Force":
    unit = st.selectbox(
        "Select Conversion",
        ["Newton to Kilogram-force", "Kilogram-force to Newton"]
    )

    if unit == "Newton to Kilogram-force":
        result = value / 9.81
        output_unit = "kgf"
    else:
        result = value * 9.81
        output_unit = "N"

elif conversion_type == "Pressure":
    unit = st.selectbox(
        "Select Conversion",
        ["Pascal to Bar", "Bar to Pascal", "PSI to Pascal", "Pascal to PSI"]
    )

    if unit == "Pascal to Bar":
        result = value / 100000
        output_unit = "bar"
    elif unit == "Bar to Pascal":
        result = value * 100000
        output_unit = "Pa"
    elif unit == "PSI to Pascal":
        result = value * 6894.76
        output_unit = "Pa"
    else:
        result = value / 6894.76
        output_unit = "psi"

else:
    unit = st.selectbox(
        "Select Conversion",
        ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
    )

    if unit == "Celsius to Fahrenheit":
        result = (value * 9 / 5) + 32
        output_unit = "°F"
    else:
        result = (value - 32) * 5 / 9
        output_unit = "°C"

st.success(f"Converted Value = {result:.4f} {output_unit}")

st.divider()

# Material Density Checker Section
st.header("🧱 Material Density Checker")

densities = {
    "Aluminum": 2700,
    "Steel": 7850,
    "Copper": 8960,
    "Brass": 8500,
    "Cast Iron": 7200,
    "Titanium": 4500,
    "Plastic": 950,
    "Wood": 700
}

material = st.selectbox("Select Material", list(densities.keys()))
density = densities[material]

st.info(f"Density of {material} = {density} kg/m³")

volume = st.number_input("Enter Volume in m³", value=1.0, min_value=0.0)
mass = density * volume

st.success(f"Mass of {material} = {mass:.2f} kg")

st.divider()

st.caption("Developed using Python and Streamlit Cloud"

import streamlit as st

def main():
    st.title("🌡️ Fahrenheit to Celsius Converter")

    # Input using Streamlit
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=32.0)

    # Convert to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Output using Streamlit
    st.write(f"🌡️ Temperature: {fahrenheit}°F = {celsius:.2f}°C")

if __name__ == '__main__':
    main()

import streamlit as st

def main():
    st.title("🔢 Square a Number")

    # Ask the user for a number using Streamlit's number input
    number = st.number_input("Type a number to see its square:", value=0.0)

    # Calculate the square
    square = number * number

    # Display the result
    st.write(f"📐 {number} squared is {square}")

if __name__ == '__main__':
    main()


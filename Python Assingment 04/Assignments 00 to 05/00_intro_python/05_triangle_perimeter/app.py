import streamlit as st

def main():
    st.title("📐 Triangle Perimeter Calculator")

    # Prompt the user for the lengths of each side
    side1 = st.number_input("What is the length of side 1?", min_value=0.0, format="%.2f")
    side2 = st.number_input("What is the length of side 2?", min_value=0.0, format="%.2f")
    side3 = st.number_input("What is the length of side 3?", min_value=0.0, format="%.2f")

    # Calculate the perimeter only if all sides are greater than 0
    if side1 > 0 and side2 > 0 and side3 > 0:
        perimeter = side1 + side2 + side3
        st.success(f"The perimeter of the triangle is {perimeter}")

if __name__ == '__main__':
    main()

import streamlit as st

def main():
    # Heading
    st.title("🐾 Favorite Animal Checker")

    # Input from user
    animal = st.text_input("Enter Your Favorite Animal:")

    # Show result only if user enters something
    if animal:
        st.success(f"Your favorite animal is {animal} 🐶🐱🦁")

# Required line to run main
if __name__ == '__main__':
    main()

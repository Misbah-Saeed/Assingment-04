import streamlit as st

def main():
    st.title("➕ Add Two Numbers")
    
    # Prompt the user for the first number (default value is 0)
    num1 = st.number_input("Enter first number:", min_value=None, max_value=None, value=0)
    
    # Prompt the user for the second number (default value is 0)
    num2 = st.number_input("Enter second number:", min_value=None, max_value=None, value=0)
    
    # Calculate the sum
    total = num1 + num2
    
    # Display the total sum
    st.write(f"The total is: {total}")

# Run the app
if __name__ == "__main__":
    main()





import streamlit as st

def main():
    st.title("🧠 Age Riddle Solver")

    # Anton's age
    Anton = 21

    # Beth is 6 years older than Anton
    Beth = Anton + 6

    # Chen is 20 years older than Beth
    Chen = Beth + 20

    # Drew is as old as Chen's age plus Anton's age
    Drew = Chen + Anton

    # Ethan is the same age as Chen
    Ethan = Chen

    # Display the results using Streamlit
    st.write(f"Anton is {Anton}")
    st.write(f"Beth is {Beth}")
    st.write(f"Chen is {Chen}")
    st.write(f"Drew is {Drew}")
    st.write(f"Ethan is {Ethan}")

if __name__ == '__main__':
    main()


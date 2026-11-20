#Final_NumberGuessing_Game using streamlit---

import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state variables
if "python_rand" not in st.session_state:
    st.session_state.python_rand = random.randint(1, 10)

if "chance" not in st.session_state:
    st.session_state.chance = 3

if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.write("Guess a number between **1 and 10**")
st.write(f"Chances left: **{st.session_state.chance}**")

user_guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=10,
    step=1
)

if st.button("Check Guess", disabled=st.session_state.game_over):

    if user_guess == st.session_state.python_rand:
        st.success("Correct guess! 🎉")
        st.session_state.game_over = True

    else:
        st.session_state.chance -= 1

        if st.session_state.chance > 0:
            st.warning("Wrong guess, try again.")
            st.info(
                f"{st.session_state.chance} chance/chances left"
            )
        else:
            st.error("Game Over!")
            st.write(
                f"The correct number was "
                f"**{st.session_state.python_rand}**"
            )
            st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.python_rand = random.randint(1, 10)
        st.session_state.chance = 3
        st.session_state.game_over = False
        st.rerun()
        
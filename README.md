# 🎯 Number Guessing Game

An interactive number guessing game built with **Python** and **Streamlit**, where players guess a secret integer between `1` and `10` within `3` chances.

## Features

- **Random Target Generation**: Picks a random number from `1` to `10` at the start of each round.
- **Limited Attempts (`3` Chances)**: Tracks remaining chances across Streamlit session state and disables further guesses once the game ends.
- **Instant Feedback**: Displays a win message on a correct guess, a warning with remaining chances on a wrong guess, or a **Game Over** message revealing the target number when chances run out.
- **Replay Support**: Shows a **Play Again** button once a round finishes to pick a new number, reset chances to `3`, and restart the game.

## Prerequisites

- Python 3.x
- Streamlit (`pip install streamlit`)

## Installation & Running

1. Save the game script as `main_3.py`.
2. Install Streamlit if you do not already have it:

   ```bash
   pip install streamlit

# Rock, Paper, Scissors Game

This Python script implements the classic game of Rock, Paper, Scissors against the computer.

## How to Use

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `rock_paper_scissors.py`).
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute it using the Python interpreter:

    ```bash
    python rock_paper_scissors.py
    ```

3.  **Play the game:**
    * The script will likely display a welcome message or a logo (if `art.py` is present).
    * You will be prompted to choose your move by typing "rock", "paper", or "scissors".
    * The computer will randomly choose its move.
    * The script will then compare your choice with the computer's choice and determine the winner of the round.
    * The outcome of the round (win, lose, or draw) will be displayed.
    * The game might continue for a set number of rounds or until you choose to quit (depending on the exact implementation in `main.py`).

## Functionality

* **User Input:** Takes the player's choice ("rock", "paper", or "scissors") as input.
* **Computer Choice:** The computer randomly selects its move from "rock", "paper", and "scissors".
* **Game Logic:** Implements the rules of Rock, Paper, Scissors to determine the winner of each round:
    * Rock beats Scissors
    * Scissors beats Paper
    * Paper beats Rock
* **Outcome Display:** Clearly displays the choices made by both the player and the computer, as well as the result of the round.
* **Scoring (Optional):** The script might keep track of the score for both the player and the computer over multiple rounds.
* **Logo Display (Optional):** If the `art.py` file (containing a `logo` string) is present in the same directory, it might be displayed at the start of the game.

## Code Structure

* `main.py` (or the name you saved it as): Contains the main game logic.
    * Likely imports the `random` module for the computer's choice.
    * Contains variables or lists to represent the possible choices.
    * Includes functions to get user input, generate the computer's choice, determine the winner, and display the results.
    * May contain a loop to allow for multiple rounds of play.
* `art.py` (optional): May contain a `logo` string for visual presentation.

## Notes

* The game provides a simple and interactive way to play Rock, Paper, Scissors against the computer.
* The computer's choice is purely random, providing an element of chance.
* Depending on the implementation in `main.py`, the game might have a specific number of rounds or allow the player to play indefinitely.
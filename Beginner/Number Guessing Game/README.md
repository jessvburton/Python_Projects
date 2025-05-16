# Number Guessing Game

This Python script implements a number guessing game where the player tries to guess a randomly generated number within a specified range (1 to 100). The game provides different difficulty levels, affecting the number of attempts allowed.

## How to Use

1.  **Save the code:**
    * Save the main script as `main.py`.
    * Save the art (logo) script as `art.py`.
        Ensure both files are in the same directory.
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the files, and execute the main script using the Python interpreter:

    ```bash
    python main.py
    ```

3.  **Play the game:**
    * The script will display a logo.
    * You'll be prompted to choose a difficulty level: "easy" or "hard".
    * The game will start, and you'll be asked to guess a number between 1 and 100.
    * After each guess, the script will tell you if your guess was "too high" or "too low".
    * You continue guessing until you guess the correct number or run out of attempts.
    * The game will then end, revealing the correct number.

## Functionality

* **Random Number Generation:** The script generates a random integer between 1 and 100 (inclusive).
* **Difficulty Levels:**
    * "Easy" mode gives the player 10 attempts.
    * "Hard" mode gives the player 5 attempts.
* **Input Handling:** The script takes integer input from the player as their guess.
* **Guess Validation:** The script checks if the player's guess is higher or lower than the actual number and provides feedback.
* **Game Termination:** The game ends when the player guesses the correct number or runs out of attempts.
* **User Interface:** The script uses the `art.py` file to display a logo at the beginning of the game and provides text-based prompts and output to the console.

## Code Structure

* `main.py`: Contains the core logic of the number guessing game.
    * `random_number`: Stores the randomly generated number.
    * `set_difficulty()`: Function to set the number of turns based on the chosen difficulty.
    * `check_answer()`: Function to compare the guess with the random number and provide feedback.
    * The main part of the script handles game setup, user input, and the game loop.
* `art.py`: Contains the `logo` string, which is used to display the game's logo.
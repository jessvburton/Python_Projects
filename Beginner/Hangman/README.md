# Hangman Game

This Python script implements the classic word-guessing game, Hangman. The player tries to guess a secret word by suggesting letters.

## How to Use

1.  **Save the code:**
    * Save the main game script as `main.py`.
    * Save the word list script as `words.py`.
    * Save the art (stages and logo) script as `art.py`.
    Ensure all three files (`main.py`, `words.py`, `art.py`) are in the same directory.
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the files, and execute the main script using the Python interpreter:

    ```bash
    python main.py
    ```

3.  **Play the game:**
    * The script will start by displaying a Hangman logo.
    * A random word will be chosen from the `word_list`.
    * You will see a display of underscores, representing the letters in the secret word.
    * You will be prompted to guess a letter.
    * If your guess is correct, the corresponding letter(s) will be revealed.
    * If your guess is incorrect, a part of the Hangman figure will be displayed, and you will lose a life.
    * The game continues until you either guess the word correctly or run out of lives.
    * At the end of the game, the secret word will be revealed, and you'll be told if you won or lost.

## Functionality

* **Word Selection:** A random word is chosen from the `word_list` located in the `words.py` file.
* **Display:** The game displays the current state of the guessed word (underscores for unguessed letters), the Hangman figure based on incorrect guesses, and the letters you have already guessed.
* **Guessing:** The player inputs one letter at a time as their guess.
* **Correct Guess:** If the guessed letter is in the secret word, all occurrences of that letter are revealed.
* **Incorrect Guess:** If the guessed letter is not in the secret word, the player loses a life, and a part of the Hangman figure is drawn.
* **Game Over:** The game ends when the player correctly guesses the word or runs out of lives (reaches the final stage of the Hangman figure).
* **Artistic Display:** The `art.py` file contains:
    * A `logo` that is displayed at the start of the game.
    * A list called `stages` which contains different ASCII art representations of the Hangman figure at various stages of completion.

## Code Structure

* `main.py`: Contains the main game logic, including:
    * Importing necessary modules and data from `words.py` and `art.py`.
    * Selecting a random word.
    * Initializing the game state (lives, display).
    * Handling user input and checking guesses.
    * Updating the display and the Hangman figure.
    * Determining the end of the game and displaying the result.
* `words.py`: Contains a list called `word_list`, which holds the words that can be chosen for the game.
* `art.py`: Contains:
    * A string variable `logo` for the game's title art.
    * A list variable `stages` containing the different stages of the Hangman figure.

## Customization

* **Word List:** You can easily customize the game by adding, removing, or modifying the words in the `word_list` within the `words.py` file.
* **Hangman Art:** You can modify the ASCII art in the `stages` list within the `art.py` file to change the appearance of the Hangman figure.
* **Number of Lives:** The number of lives the player has can be adjusted within the `main.py` script.
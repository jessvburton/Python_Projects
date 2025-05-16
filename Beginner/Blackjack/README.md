# Blackjack Game

This Python project contains two implementations of a simple Blackjack card game:

* `main_with-hints.py`
* `main_without-hints.py`

## How to Use

1.  **Save the code:** Save either of the Python scripts (`blackjack_with_hints.py` or `blackjack.py`) as a `.py` file.
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute it using the Python interpreter:

    ```bash
    python blackjack.py  # Or python blackjack_with_hints.py
    ```

3.  **Play the game:**
    * The game will start by dealing cards.
    * You'll be prompted to decide whether to "hit" (take another card) or "stand" (pass).
    * The computer (dealer) will play according to the game rules.
    * The script will determine and display the winner.
    * You'll be given the option to play another round.

## Our Blackjack House Rules

-   The deck is unlimited in size.
-   There are no jokers.
-   The Jack/Queen/King all count as 10.
-   The Ace can count as 11 or 1.
-   Use the following list as the deck of cards:
    -   `cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
-   The cards in the list have an equal probability of being drawn.
-   Cards are not removed from the deck as they are drawn.
-   The computer is the dealer.

## Functionality

Both scripts implement the following core Blackjack functionality:

* **Card Dealing:** Randomly selecting cards from the `cards` list.
* **Score Calculation:** Calculating the total value of a hand, with Ace handling.
* **Determining the Winner:** Comparing player and computer scores, considering busts and Blackjack.
* **Game Loop:** Managing the flow of the game, user input, and computer's turn.
* **User Interface:** Providing text-based prompts and output to the console.

## Code Structure

Key elements in the code include:

* `cards`:  The list representing the deck.
* `user_cards` / `player1`, `computer_cards` / `computer`: Lists to store the cards for each player.
* Functions for dealing cards, calculating scores, and comparing results.
* A main game function (`blackjack()`) to orchestrate the gameplay.

## Author's Notes

For this challenge, I first attempted it without using any of the hints (`main_without-hints.py`). By doing it this way, I learned a lot and faced many challenges, some of which I overcame, while others I did not. The code runs, but does not perfectly adhere to all of the house rules.

For my second attempt, I used the hints provided (`main_with-hints.py`) and completed the challenge fairly quickly. Seeing the different ways the code can be compiled was very educational and helpful.
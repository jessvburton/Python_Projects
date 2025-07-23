# Pong Game

This Python script implements the classic arcade game Pong using the `turtle` graphics library. Two players (one controlled by the user, the other by the computer or a second user) control paddles to hit a ball back and forth, trying to prevent the opponent from scoring.

## How to Use

1.  **Save the code:** Save the Python files with the following names:
    * `main.py`
    * `ball.py`
    * `paddle.py`
    * `scoreboard.py`
    Ensure all files are in the same directory.
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the files, and execute the main script using the Python interpreter. This will open a graphical window:

    ```bash
    python main.py
    ```

3.  **Control your paddle:**
    * The controls for the left paddle are typically the **"w" key (up)** and the **"s" key (down)**.
    * The controls for the right paddle are typically the **"Up arrow key (↑)" (up)** and the **"Down arrow key (↓)" (down)**.
    * Press these keys to move your paddle vertically.

4.  **Play the game:**
    * The ball will start moving.
    * Use your paddle to hit the ball back towards your opponent.
    * The goal is to make your opponent miss the ball, allowing it to go past their paddle and score a point for you.
    * The scoreboard will update after each point.
    * The game will likely continue until one player reaches a certain score.

## Functionality

* **Object Creation:** Uses the `turtle` library to create the game elements:
    * **Ball:** The object that moves across the screen and needs to be hit by the paddles.
    * **Paddles:** Rectangular objects controlled by the players to intercept the ball.
    * **Scoreboard:** Displays the scores of both players.
* **Paddle Control:** Allows users to move their paddles up and down using keyboard input.
* **Ball Movement:** Controls the ball's speed and direction. The ball's trajectory might change upon hitting a paddle.
* **Collision Detection:** Detects collisions between the ball and the paddles, as well as the top and bottom walls.
* **Scoring:** Increments the score of a player when the opponent fails to hit the ball.
* **Game Over Condition:** The game likely ends when one player reaches a predetermined winning score.

## Code Structure

* `main.py`: This is the main script that initializes the game, creates the game objects, and manages the game loop. It handles user input, ball movement, collision detection, and scoring.
* `ball.py`: Defines the `Ball` class, which controls the ball's attributes (shape, color, speed, movement) and behavior (bouncing).
* `paddle.py`: Defines the `Paddle` class, which controls the paddles' attributes (shape, color, size, movement) and their response to user input.
* `scoreboard.py`: Defines the `Scoreboard` class, which manages the score, updates the display on the screen, and potentially determines the winner.

## Notes

* Ensure you have a graphical environment set up to run the `turtle` library.
* The game speed and difficulty can be adjusted by modifying parameters within the scripts (e.g., ball speed, paddle speed).
* This is a fundamental implementation of Pong and can be expanded with more features like sound effects, different game modes, or AI opponents.
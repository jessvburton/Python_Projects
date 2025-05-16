# Turtle Crossing Game

This Python script implements a game where the player controls a turtle that needs to cross a busy road without getting hit by cars. The goal is to reach the finish line on the other side.

## How to Use

1.  **Save the code:** Save the Python files with the following names:
    * `main.py`
    * `player.py`
    * `car_manager.py`
    * `scoreboard.py`
    Ensure all files are in the same directory.
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the files, and execute the main script using the Python interpreter. This will open a graphical window:

    ```bash
    python main.py
    ```

3.  **Control the turtle:** Use the **"Up arrow key (↑)"** to move the turtle forward across the road.

4.  **Play the game:**
    * The turtle will start at the bottom of the screen.
    * Cars will be generated and move across the screen at varying speeds.
    * Avoid colliding with the cars. If the turtle gets hit, the game ends.
    * When the turtle successfully reaches the top of the screen, you level up, the cars move faster, and the game continues.
    * The scoreboard will track your current level.

## Functionality

* **Object Creation:** Uses the `turtle` library to create the game elements:
    * **Player (Turtle):** The character controlled by the user.
    * **Cars:** Obstacles that move across the screen.
    * **Scoreboard:** Displays the current level of the player.
* **Player Control:** Allows the user to move the turtle forward using keyboard input.
* **Car Generation and Movement:** Randomly generates cars with different colors and speeds that move across the screen.
* **Collision Detection:** Detects when the turtle collides with a car, ending the game.
* **Level Progression:** When the turtle reaches the finish line, the game level increases, and the difficulty (car speed) is typically increased.
* **Scorekeeping:** Tracks and displays the player's current level on the scoreboard.
* **Game Over:** Ends the game when a collision occurs and displays a "Game Over" message.

## Code Structure

* `main.py`: This is the main script that initializes the game, creates the game objects (player, car manager, scoreboard), and manages the game loop. It handles user input, car movement, collision detection, level progression, and game over conditions.
* `player.py`: Defines the `Player` class, which controls the turtle's attributes (starting position, movement) and its ability to reach the finish line.
* `car_manager.py`: Defines the `CarManager` class, which is responsible for generating cars, controlling their speed and movement across the screen, and managing the list of active cars.
* `scoreboard.py`: Defines the `Scoreboard` class, which keeps track of the player's level and displays it on the screen. It also displays the "Game Over" message.

## Notes

* Ensure you have a graphical environment set up to run the `turtle` library.
* The game's difficulty increases with each level as the cars move faster.
* This is a classic arcade-style game that tests the player's reflexes and timing.
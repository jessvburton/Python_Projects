# Turtle Racing Game

This Python script implements a simple turtle racing game using the `turtle` graphics library. Multiple turtles race across the screen, and the player can place a bet on which turtle they think will win.

## How to Use

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `turtle_race.py`).
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute it using the Python interpreter. This will open a graphical window:

    ```bash
    python main.py
    ```

3.  **Place your bet:** The script will likely prompt you to choose a turtle color to bet on. Enter the color of the turtle you think will win the race.

4.  **Watch the race:** Several turtles with different colors will start at the left side of the screen and race towards the right. Their movement is randomized.

5.  **See the result:** Once a turtle crosses the finish line, the game will announce the winning turtle's color, and it will tell you if you won your bet.

6.  **Close the window:** Close the turtle graphics window to exit the program.

## Functionality

* **Turtle Graphics:** Utilizes the `turtle` library to create and animate multiple turtle objects.
* **Multiple Racers:** Creates several turtles, each with a distinct color.
* **Random Movement:** Assigns random forward movements to each turtle in each step of the race, making the outcome unpredictable.
* **User Betting:** Allows the player to bet on a specific turtle color before the race begins.
* **Winner Determination:** Identifies and announces the turtle that reaches the finish line first.
* **Bet Result:** Informs the player whether their chosen turtle won the race.

## Code Structure

* `main.py` (or the name you saved it as): Contains the main logic of the turtle racing game.
    * Imports the `turtle` and `random` libraries.
    * Creates a `Screen` object to set up the racing window.
    * Prompts the user to place a bet on a turtle color.
    * Creates multiple `Turtle` objects, assigning them different colors and starting positions.
    * Implements a loop that makes each turtle move forward by a random distance in each iteration.
    * Checks if any turtle has reached the finish line.
    * Once a winner is determined, it announces the winning color and compares it to the user's bet.
    * `screen.exitonclick()` keeps the window open until it is manually closed.

## Notes

* Ensure you have a graphical environment set up to run the `turtle` library.
* The number of racing turtles and their colors can be easily modified within the script.
* The speed of the race is determined by the random distances assigned to each turtle's movement.
* This is a simple and fun game that demonstrates basic animation and user interaction with the `turtle` library.
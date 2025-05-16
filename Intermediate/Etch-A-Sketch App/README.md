
# Etch-A-Sketch

This Python script simulates a basic Etch-A-Sketch toy using the `turtle` graphics library. You can control a "turtle" on the screen to draw lines by pressing specific keys.

## How to Use

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `etch_a_sketch.py`).
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute it using the Python interpreter. This will open a graphical window:

    ```bash
    python etch_a_sketch.py
    ```

3.  **Control the turtle:** Use the following keys to control the drawing:
    * **W:** Move forward
    * **S:** Move backward
    * **A:** Turn left
    * **D:** Turn right
    * **C:** Clear the drawing

4.  **Close the window:** Close the turtle graphics window to exit the program.

## Functionality

* **Turtle Graphics:** Utilizes the `turtle` library to create and control a drawing pen on the screen.
* **Movement Control:** Allows the user to move the turtle forward and backward.
* **Turning:** Enables the user to rotate the turtle left and right by a small angle.
* **Clearing the Screen:** Provides a function to reset the drawing and the turtle's position to the center.
* **Event Handling:** Uses the `screen.listen()` method to detect key presses and associate specific functions with each key.

## Code Structure

* `main.py` (or the name you saved it as): Contains the main logic of the Etch-A-Sketch program.
    * Imports the `turtle` library.
    * Creates a `Turtle` object and a `Screen` object.
    * Defines functions for moving forward (`move_forwards`), moving backward (`move_backwards`), turning left (`turn_left`), turning right (`turn_right`), and clearing the screen (`clear_screen`).
    * Uses `screen.onkey()` to bind these functions to the 'w', 's', 'a', 'd', and 'c' keys respectively.
    * The `screen.listen()` method starts listening for keyboard events.
    * `screen.exitonclick()` keeps the window open until it is manually closed.

## Notes

* Ensure you have a graphical environment set up to run the `turtle` library.
* The drawing speed and turning angle can be adjusted by modifying the values within the defined functions.
* This is a basic implementation of an Etch-A-Sketch and can be expanded with more features like changing pen color, pen size, or adding the ability to lift the pen.
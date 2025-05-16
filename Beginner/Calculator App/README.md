# Simple Calculator App

This Python script implements a basic calculator that allows users to perform arithmetic operations: addition, subtraction, multiplication, and division.

## How to Use

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `calculator.py`).
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute it using the Python interpreter:

    ```bash
    python calculator.py
    ```

3.  **Perform calculations:**
    * The script will first display a logo (if `art.py` is in the same directory).
    * It will then present the available operations: `+`, `-`, `*`, `/`.
    * You will be prompted to enter the first number.
    * You will then be asked to pick an operation.
    * Next, you will be prompted to enter the second number.
    * The script will calculate and display the result.
    * You will have the option to perform another calculation using the previous result or start a new calculation.

## Functionality

* **Basic Arithmetic Operations:** Supports addition (+), subtraction (-), multiplication (\*), and division (/).
* **User Input:** Takes numerical input from the user for calculations.
* **Operation Selection:** Allows the user to choose the desired arithmetic operation.
* **Sequential Calculations:** Provides an option to continue calculating with the previous result.
* **Clear Output:** Displays the calculation steps and the final answer in a user-friendly format.
* **Logo Display:** If the `art.py` file (containing a `logo` string) is present in the same directory, it will be displayed at the start of the application.

## Code Structure

* `main.py` (or the name you saved it as): Contains the main logic of the calculator.
    * Includes functions for each arithmetic operation (`add`, `subtract`, `multiply`, `divide`).
    * The main part of the script handles user input, calls the appropriate operation function, and manages the flow of calculations.
    * It also includes logic for continuing calculations and starting new ones.
    * It attempts to import and display the `logo` from `art.py` if available.
* `art.py` (optional): May contain a `logo` string for visual presentation.

## Notes

* The script includes basic error handling for division by zero.
* It expects numerical input from the user. Entering non-numeric input may lead to errors.
* This is a simple calculator application demonstrating basic input/output and arithmetic operations in Python.
# Tip Calculator

This Python script calculates the amount each person should pay when splitting a bill, including a tip. It prompts the user for the total bill amount, the desired tip percentage, and the number of people sharing the bill.

## How to Use

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `tip_calculator.py`).
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute it using the Python interpreter:

    ```bash
    python tip_calculator.py
    ```

3.  **Provide input:** The script will ask you the following questions:
    * "What was the total bill?" - Enter the total amount of the bill.
    * "What percentage tip would you like to give? 10%, 12%, or 15%?" - Enter the desired tip percentage (10, 12, or 15).
    * "How many people to split the bill?" - Enter the number of people sharing the bill.

4.  **View the result:** The script will calculate and display the amount each person should pay, formatted to two decimal places.

## Functionality

* **User Input:** Takes the total bill amount, tip percentage, and the number of people as input from the user.
* **Tip Calculation:** Calculates the tip amount based on the provided percentage.
* **Bill Splitting:** Divides the total bill (including the tip) by the number of people to determine the amount each person owes.
* **Formatted Output:** Displays the final amount per person, formatted to two decimal places for currency representation.

## Code Structure

* `main.py` (or the name you saved it as): Contains the main logic of the tip calculator.
    * Prompts the user for input using the `input()` function.
    * Performs the necessary calculations to determine the tip and the amount per person.
    * Formats the final result using an f-string and the `:.2f` format specifier.
    * Prints the result to the console.

## Notes

* The script assumes that the user will enter valid numerical input.
* The tip percentages are limited to 10%, 12%, or 15%, but the code can be easily modified to allow for other percentages.
* This is a simple script that demonstrates basic arithmetic operations and user input/output in Python.
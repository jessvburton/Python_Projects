# Password Generator

This Python script generates strong and random passwords based on user-specified criteria, including the desired number of letters, symbols, and numbers.

## How to Use

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `password_generator.py`).
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute it using the Python interpreter:

    ```bash
    python password_generator.py
    ```

3.  **Answer the prompts:**
    * The script will first display a logo (if `art.py` is in the same directory).
    * You will be asked a series of questions:
        * How many letters would you like in your password?
        * How many symbols would you like?
        * How many numbers would you like?
    * Enter the desired number for each prompt and press Enter.
    * The script will then generate and display a strong, randomly generated password based on your specifications.

## Functionality

* **User-Defined Length:** Allows the user to specify the desired number of letters, symbols, and numbers in the password.
* **Random Character Selection:** Randomly selects characters from predefined lists of letters (both uppercase and lowercase), symbols, and numbers.
* **Password Generation:** Combines the randomly selected characters to create a password of the specified length and composition.
* **Shuffling:** Shuffles the order of the characters in the generated password to ensure randomness and security.
* **Logo Display:** If the `art.py` file (containing a `logo` string) is present in the same directory, it will be displayed at the start of the application.

## Code Structure

* `main.py` (or the name you saved it as): Contains the main logic of the password generator.
    * Imports the `random` module for random character selection and shuffling.
    * Defines lists of letters, symbols, and numbers.
    * Prompts the user for the desired password composition.
    * Uses list comprehensions and the `random.choice()` function to generate random characters.
    * Combines the characters into a list and uses `random.shuffle()` to randomize their order.
    * Prints the generated password to the console.
    * Attempts to import and display the `logo` from `art.py` if available.
* `art.py` (optional): May contain a `logo` string for visual presentation.

## Notes

* Using a combination of letters (uppercase and lowercase), symbols, and numbers significantly increases the strength and security of the generated password.
* The `random.shuffle()` function ensures that the order of characters is unpredictable.
* This script provides a simple way to generate strong passwords for various online accounts and services.
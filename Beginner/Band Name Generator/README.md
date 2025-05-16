# Band Name Generator

This Python script generates a band name based on user input. It prompts the user for the city they grew up in and the name of their pet, then combines these two strings to suggest a band name.

## How to Use

1.  **Save the code:** Save the Python code as a `.py` file (e.g., `band_name.py`).
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute the script using the Python interpreter:

    ```bash
    python band_name.py
    ```

3.  **Provide input:** The script will ask you two questions:
    * "What city did you grow up in?"
    * "What is the name of your pet?"
    
    Enter the appropriate information and press Enter after each.

4.  **View the generated name:** The script will then display a suggested band name by combining your city and pet's name.

    ```
    Welcome to the band name generator!
    What city did you grow up in?
    London
    What is the name of your pet?
    Buddy
    Your band name could be London Buddy
    ```

## Functionality

The script performs the following actions:

1.  **Greets the user:** Prints a welcome message to the console.
2.  **Gets user input:**
    * Prompts the user to enter the name of the city they grew up in and stores the input in the `city` variable.
    * Prompts the user to enter the name of their pet and stores the input in the `name` variable.
3.  **Generates band name:** Concatenates the `city` and `name` strings, separated by a space, and stores the result in the `band` variable.
4.  **Displays output:** Prints the generated band name to the console using an f-string for clear formatting.

##  Additional Notes

* The script provides a simple and fun way to generate band names based on personal information.
* The generated name is a straightforward combination of the provided inputs without any additional processing or creative manipulation.

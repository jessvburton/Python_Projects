# Caesar Cipher

This Python script implements the Caesar Cipher, a simple method of encryption that shifts each letter in a text by a fixed number of positions down the alphabet.

## How to Use

1.  **Save the code:**
    * Save the main script as `main.py`.
    * Save the art (logo) script as `art.py`.  Ensure both files are in the same directory.
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the files, and execute the main script using the Python interpreter:

    ```bash
    python main.py
    ```

3.  **Follow the prompts:**
    * The script will display a logo.
    * You'll be asked to type either "encode" to encrypt a message or "decode" to decrypt a message.
    * You'll then be prompted to enter the message you want to encrypt or decrypt.
    * Finally, you'll be asked to enter the "shift number," which determines how many positions each letter is shifted.
    * The script will output the encoded or decoded text.
    * You'll be asked if you want to go again.

## Functionality

* **Encryption:** Shifts each letter in the input text forward by the specified shift amount.  Letters wrap around from the end of the alphabet to the beginning (e.g., shifting 'z' by 1 results in 'a').
* **Decryption:** Shifts each letter in the input text backward by the specified shift amount (the inverse of encryption).
* **Case Preservation:** The script handles both uppercase and lowercase letters, preserving their case during the encryption/decryption process.
* **Non-alphabetic Character Handling:** Characters that are not letters (e.g., numbers, symbols, spaces) are left unchanged.
* **Modular Arithmetic:** Uses the modulo operator (%) to handle wrap-around when shifting letters beyond the boundaries of the alphabet.
* **User Interaction:** The script prompts the user for input (direction, text, shift) and provides output to the console.
* **Looping:** Allows the user to perform multiple encoding/decoding operations until they choose to exit.
* **Artistic Flair:** Includes an `art.py` file to display a logo at the beginning of the program.

## Code Structure

* `main.py`: Contains the core logic of the Caesar Cipher.
    * `alphabet`: A list of lowercase letters.
    * `alpha`: A list of uppercase letters.
    * `caesar(direction, text, shift)`:  A function that performs either encryption or decryption based on the `direction` argument.
    * The main part of the script handles user input, calls the `caesar` function, and controls the program loop.
* `art.py`:  Contains the `logo` string, which is used to display the Caesar Cipher logo.

## Notes

* The shift value can be any integer.  A large shift value is handled correctly due to the modulo operator.
* This is a simple substitution cipher and is not considered cryptographically secure for protecting sensitive information.
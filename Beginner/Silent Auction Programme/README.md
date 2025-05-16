# Silent Auction Program

This Python script simulates a silent auction, allowing multiple users to enter their names and bids for an item. The program then determines the highest bid and declares the winner.

## How to Use

1.  **Save the code:**
    * Save the main script as `main.py`.
    * Save the art (logo) script as `art.py`.
        Ensure both files are in the same directory.
2.  **Install the `replit` library (if necessary):** If you are using Replit to run this code, you don't need to install anything. Otherwise, you might need to install the `replit` library to use the `clear()` function. You can do this using pip:

    ```bash
    pip install replit
    ```

3.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the files, and execute the main script using the Python interpreter:

    ```bash
    python main.py
    ```

4.  **Participate in the auction:**
    * The script will display a logo.
    * You will be prompted to enter your name and your bid amount.
    * The script will ask if there are other bidders.
    * If there are, the screen will clear (if the `replit` library is available), and the next bidder can enter their information.
    * If there are no more bidders, the script will determine and display the name of the winner and the highest bid.

## Functionality

* **Data Storage:** Uses a dictionary (`auction`) to store the names of bidders and their corresponding bids.
* **User Input:** Prompts bidders to enter their names and bid amounts.
* **Bid Tracking:** Keeps track of the highest bid entered so far.
* **Winner Determination:** After all bids are collected, the script iterates through the bids to identify the highest bid and the corresponding bidder.
* **Clear Screen (Optional):** Uses the `replit.clear()` function to clear the console screen between bidders (this requires the `replit` library).
* **Logo Display:** Displays a logo at the beginning of the program using the `art.py` file.

## Code Structure

* `main.py`: Contains the main logic of the silent auction program.
    * Imports the `art` module (for the logo) and the `replit` module (for clearing the screen).
    * Initializes variables to store auction data (e.g., `auction` dictionary, `highest_bid`, `winner`).
    * Defines a function `bidder()` to collect bidder information (name and bid).
    * Uses a `while` loop to control the auction process, allowing multiple bidders to participate.
    * Determines the winner after all bidders have entered their bids.
* `art.py`: Contains the `logo` string, which is used to display the auction logo.

## Notes

* The script assumes that bids are numerical values.
* The `replit.clear()` function may not work in all environments. If it doesn't, the screen won't clear between bidders, but the program will still function correctly.
* This is a basic implementation of a silent auction and can be extended to include features like item descriptions, bid increments, or time limits.
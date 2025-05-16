# Coffee Machine

This Python program simulates a coffee machine that can make different types of coffee (latte, espresso, cappuccino). It manages resources (water, milk, coffee), processes payments, and provides a user interface to order drinks.

## How to Use

1.  **Save the code:** Save the Python files with the following names:
    * `main.py`
    * `coffee_maker.py`
    * `menu.py`
    * `money_machine.py`
2.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the files, and execute the main script using the Python interpreter:

    ```bash
    python main.py
    ```

3.  **Interact with the machine:**
    * The program will display a list of available drinks.
    * You can order a drink by typing its name (e.g., "latte").
    * The machine will check if there are enough resources to make the drink.
    * If resources are sufficient, you will be prompted to insert coins.
    * The machine will process the payment and, if successful, dispense the drink.
    * You can also type "report" to see the current resource levels and money earned or "off" to turn off the machine.

## Functionality

* **Drink Selection:** Offers a menu of coffee drinks (latte, espresso, cappuccino), each with specific ingredient requirements and costs.
* **Resource Management:** Tracks the available quantities of water, milk, and coffee. Prevents orders from being fulfilled if there are insufficient resources.
* **Payment Processing:** Handles coin input from the user, calculates the total amount, and determines if it's enough to cover the drink cost. Provides change if necessary.
* **Report Generation:** Displays a report of the current resource levels and the machine's earnings.
* **Machine Control:** Allows turning the machine on or off.

## Code Structure

The program is organized into several classes and modules:

* `main.py`: This is the main script that runs the coffee machine.
    * It initializes the `CoffeeMaker`, `MoneyMachine`, and `Menu` objects.
    * It provides the main loop for user interaction, taking orders, processing payments, and making coffee.
* `menu.py`: Defines the `MenuItem` and `Menu` classes.
    * `MenuItem` represents a single drink item with its name, ingredients, and cost.
    * `Menu` manages the list of available drinks and provides methods to find drinks by name and get a list of all drink names.
* `coffee_maker.py`: Defines the `CoffeeMaker` class, which handles the coffee-making process.
    * It tracks the machine's resources (water, milk, coffee).
    * It checks if there are enough resources to make a drink.
    * It deducts the required ingredients when a drink is made.
    * It provides a report of the current resource levels.
* `money_machine.py`: Defines the `MoneyMachine` class, which handles the financial aspects.
    * It processes coin inputs.
    * It calculates the total money received.
    * It checks if the payment is sufficient.
    * It manages the machine's profit.
    * It provides a report of the money earned.

## Classes

* **MenuItem:** Represents a single item on the menu (e.g., "latte"). Stores the drink's name, cost, and required ingredients.
* **Menu:** Manages a collection of `MenuItem` objects. Provides methods to access and find drinks.
* **CoffeeMaker:** Simulates the coffee-making hardware. Tracks resources and makes drinks.
* **MoneyMachine:** Handles the money transactions. Processes payments and tracks profit.
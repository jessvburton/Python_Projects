from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))
    for sign in operations:
        print(sign)

    math = True

    while math == True:
        operation_sign = input("Pick an operation from the lines above: ")
        num2 = float(input("What is the next number?: "))

        calculation_function = operations[operation_sign]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")

        go_on = input(
            f"Type 'y' to continue calculating with {answer}, 'n' to exit or 'r' to start a new calculation: "
        ).lower()
        if go_on == "y":
            num1 = answer
        elif go_on == "r":
            math = False
            calculator()
        else:
            math = False


calculator()

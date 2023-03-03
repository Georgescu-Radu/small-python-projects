from art import logo

def add(n1, n2):
    """Adds two numbers (n1 and n2)"""
    return n1 + n2


def subtract(n1, n2):
    """Subtracts n2 from n1"""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers (n1 and n2)"""
    return n1 * n2


def divide(n1, n2):
    """Divides two numbers (n1 and n2)"""
    return n1 / n2


# Daca puneam parantezele functiilor in dictionar, le apela pe toate in background chiar daca eu nu le afisam
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
print(logo)
num1 = float(input("What's the first number? "))
for symbol in operations:
    print(symbol)
go_again = "y"
i = 1
while go_again == "y":
    operation_symbol = input("Chose an operation: ")
    num2 = float(input("What's the next number? "))
    if i == 1:
        first_answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        go_again = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit. ")
    else:
        second_answer = operations[operation_symbol](first_answer, num2)
        print(f"{first_answer} {operation_symbol} {num2} = {second_answer}")
        go_again = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit. ")
    i += 1

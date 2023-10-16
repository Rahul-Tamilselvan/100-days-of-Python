# Recursion

# add
def add(n1, n2):
    return n1 + n2

# sub
def sub(n1, n2):
    return n1 - n2

# Multiply
def mul(n1, n2):
    return n1 * n2

# Divide
def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    num1 = float(input("what is the first number ? : "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("what is the next number ? : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
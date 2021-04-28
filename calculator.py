"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

"""
if first token is 'pow':
	evaluate as power function

2nd & 3rd tokens as arguments

repeat forever:
    read input
    tokenize input
        if the first token is "q":
            quit
        else:
            (decide which math function to call based on first token)
            if the first token is 'pow':
                  call the power function with the other two tokens

            (...etc.)

"""

while True:
    user_input = input ("Please provide an equation you would like me to solve. >")
    tokens = user_input.split(" ")
    if tokens[0] == "q":
        print("Thanks for playing. CLOSE CALCULATOR.")
        break
    elif len(tokens) == 2:
        tokens[1] = int(tokens[1])
        if tokens[0] == "square":
            result = square(tokens[1])
        elif tokens[0] == "cube":
            result = cube(tokens[1])
    elif len(tokens) == 3:
        tokens[1] = int(tokens[1])
        tokens[2] = int(tokens[2])
        if tokens[0] == "+":
            result = add(tokens[1],tokens[2])
        elif tokens[0] == "-":
            result = subtract(tokens[1],tokens[2])
        elif tokens[0] == "*":
            result = multiply(tokens[1],tokens[2])
        elif tokens[0] == "/":
            result = divide(tokens[1],tokens[2])
        elif tokens[0] == "pow":
            result = power(tokens[1],tokens[2])
        elif tokens[0] == "mod":
            result = mod(tokens[1],tokens[2])
    print(result)
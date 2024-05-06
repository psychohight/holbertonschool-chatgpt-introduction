#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): The non-negative integer for which to compute the factorial.

    Returns:
    int: The factorial of the number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Main program execution starts here
if len(sys.argv) > 1:
    try:
        input_number = int(sys.argv[1])
        if input_number < 0:
            print("Please enter a non-negative integer.")
        else:
            f = factorial(input_number)
            print(f)
    except ValueError:
        print("Please enter a valid integer.")
else:
    print("No number provided. Please provide a number as an argument.")


# math_operations.py

def add(x, y): return x + y

def subtract(x, y): return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

## this comment is wrong

def print_jordan():
    print("jordan")

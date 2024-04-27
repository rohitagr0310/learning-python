import time


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"


if __name__ == "__main__":
    # Input values
    a = 10
    b = 5

    # Start time
    start_time = time.time()

    # Perform arithmetic operations
    add_result = add(a, b)
    subtract_result = subtract(a, b)
    multiply_result = multiply(a, b)
    divide_result = divide(a, b)

    # End time
    end_time = time.time()

    # Print execution time
    print("Normal - Execution time:", end_time - start_time, "seconds")

import threading
import time


def add(a, b, result_list):
    result_list.append(a + b)


def subtract(a, b, result_list):
    result_list.append(a - b)


def multiply(a, b, result_list):
    result_list.append(a * b)


def divide(a, b, result_list):
    if b != 0:
        result_list.append(a / b)
    else:
        result_list.append("Error: Division by zero")


if __name__ == "__main__":
    # Input values
    a = 10
    b = 5

    # List to store results
    results = []

    # Start time
    start_time = time.time()

    # Create threads for each arithmetic operation
    threads = [
        threading.Thread(target=add, args=(a, b, results)),
        threading.Thread(target=subtract, args=(a, b, results)),
        threading.Thread(target=multiply, args=(a, b, results)),
        threading.Thread(target=divide, args=(a, b, results)),
    ]

    # Start each thread
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # End time
    end_time = time.time()

    # Print execution time
    print("Multi Threading - Execution time:", end_time - start_time, "seconds")

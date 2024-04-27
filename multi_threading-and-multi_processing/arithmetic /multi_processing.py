import multiprocessing
import time


def add(a, b, result_queue):
    result_queue.put(a + b)


def subtract(a, b, result_queue):
    result_queue.put(a - b)


def multiply(a, b, result_queue):
    result_queue.put(a * b)


def divide(a, b, result_queue):
    if b != 0:
        result_queue.put(a / b)
    else:
        result_queue.put("Error: Division by zero")


if __name__ == "__main__":
    # Input values
    a = 10
    b = 5

    # Create a multiprocessing Queue to store results
    result_queue = multiprocessing.Queue()

    # Create processes for each arithmetic operation
    processes = [
        multiprocessing.Process(target=add, args=(a, b, result_queue)),
        multiprocessing.Process(target=subtract, args=(a, b, result_queue)),
        multiprocessing.Process(target=multiply, args=(a, b, result_queue)),
        multiprocessing.Process(target=divide, args=(a, b, result_queue)),
    ]

    # Start time
    start_time = time.time()

    # Start each process
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # End time
    end_time = time.time()

    # Print execution time
    print("Multi Processing - Execution time:", end_time - start_time, "seconds")

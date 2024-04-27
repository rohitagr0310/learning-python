import numpy as np
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import time
import threading
import multiprocessing

# Generate synthetic regression dataset
X, y = make_regression(n_samples=10000, n_features=20, noise=0.1, random_state=42)

# Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Function to make predictions using RandomForestRegressor
def make_predictions(model, X, result_list):
    result_list.extend(model.predict(X))


if __name__ == "__main__":
    # Create RandomForestRegressor model
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    model.fit(X_train, y_train)
    # Single-threaded prediction
    start_time = time.time()
    predictions_single = make_predictions(model, X_test, [])
    end_time = time.time()
    print("Single-threaded prediction time:", end_time - start_time, "seconds")

    # Multithreading prediction
    num_threads = 4  # Number of threads
    chunk_size = len(X_test) // num_threads  # Divide data into chunks
    threads = []
    results = []
    for i in range(num_threads):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size if i < num_threads - 1 else len(X_test)
        thread = threading.Thread(
            target=make_predictions, args=(model, X_test[start_idx:end_idx], results)
        )
        threads.append(thread)
    start_time = time.time()  # Start measuring time just before starting threads
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()  # Stop measuring time after all threads have finished
    print("Multithreading prediction time:", end_time - start_time, "seconds")

    # Multiprocessing prediction
    num_processes = 4  # Number of processes
    chunk_size = len(X_test) // num_processes  # Divide data into chunks
    processes = []
    manager = multiprocessing.Manager()
    results = manager.list()
    for i in range(num_processes):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size if i < num_processes - 1 else len(X_test)
        process = multiprocessing.Process(
            target=make_predictions, args=(model, X_test[start_idx:end_idx], results)
        )
        processes.append(process)
    start_time = time.time()  # Start measuring time just before starting processes
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()  # Stop measuring time after all processes have finished
    print("Multiprocessing prediction time:", end_time - start_time, "seconds")

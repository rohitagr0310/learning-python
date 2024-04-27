from PIL import Image
import os
import multiprocessing
import time


def grayscale_image(image_path):
    image = Image.open(image_path).convert("L")
    image.save(os.path.join("output", os.path.basename(image_path)))


def process_images(image_files):
    for image_file in image_files:
        grayscale_image(image_file)


if __name__ == "__main__":
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # List of image file paths
    image_files = [f"images/image{i}.jpg" for i in range(1, 1001)]

    # Start time
    start_time = time.time()

    # Number of processes
    num_processes = 8

    # Divide image files into chunks for each process
    chunk_size = len(image_files) // num_processes
    chunks = [
        image_files[i : i + chunk_size] for i in range(0, len(image_files), chunk_size)
    ]

    # Create and start processes
    processes = []
    for chunk in chunks:
        process = multiprocessing.Process(target=process_images, args=(chunk,))
        process.start()
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # End time
    end_time = time.time()

    # Print execution time
    print("Multiprocessing execution time:", end_time - start_time, "seconds")

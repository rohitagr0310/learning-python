from PIL import Image
import os
import time


def grayscale_image(image_path):
    image = Image.open(image_path).convert("L")
    image.save(os.path.join("output", os.path.basename(image_path)))


if __name__ == "__main__":
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # List of image file paths
    image_files = [f"images/image{i}.jpg" for i in range(1, 1001)]

    # Start time
    start_time = time.time()

    # Process images sequentially
    for image_file in image_files:
        grayscale_image(image_file)

    # End time
    end_time = time.time()

    # Print execution time
    print("Single-threaded execution time:", end_time - start_time, "seconds")

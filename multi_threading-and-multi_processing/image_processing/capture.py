import cv2
import os

if __name__ == "__main__":
    # Create output directory if it doesn't exist
    os.makedirs("captured_images", exist_ok=True)

    # Initialize camera
    camera = cv2.VideoCapture(
        0
    )  # Change 0 to the index of your camera if you have multiple cameras

    # Check if camera opened successfully
    if not camera.isOpened():
        print("Error: Unable to open camera")
        exit()

    # Capture 1000 images
    for i in range(1, 1001):
        # Capture frame-by-frame
        ret, frame = camera.read()

        if not ret:
            print("Error: Unable to capture frame")
            break

        # Save the captured frame as an image
        image_path = os.path.join("captured_images", f"image{i}.jpg")
        cv2.imwrite(image_path, frame)

        print(f"Image {i} captured and saved")

    # Release the camera
    camera.release()

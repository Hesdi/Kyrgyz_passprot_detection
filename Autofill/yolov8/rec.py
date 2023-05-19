import cv2
import numpy as np
import time

# Define the dimensions of the rectangle
rectangle_width = 400
rectangle_height = 300

# Define the desired video width and height
video_width = 1080
video_height = 720

# Initialize the camera
camera = cv2.VideoCapture(0)

# Set the camera resolution
camera.set(cv2.CAP_PROP_FRAME_WIDTH, video_width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, video_height)

# Set the time interval for capturing images (in seconds)
capture_interval = 2

# Initialize the timestamp for capturing images
last_capture_time = time.time()

while True:
    # Read a frame from the camera
    ret, frame = camera.read()

    # Get the dimensions of the frame
    frame_height, frame_width = frame.shape[:2]

    # Create a mask with the same dimensions as the frame
    mask = np.zeros_like(frame, dtype=np.uint8)

    # Calculate the coordinates for the rectangle
    x = (frame_width - rectangle_width) // 2
    y = (frame_height - rectangle_height) // 2

    # Draw a white rectangle on the mask to highlight the center area
    cv2.rectangle(mask, (x, y), (x + rectangle_width, y + rectangle_height), (255, 255, 255), -1)

    # Create a mask for the area inside the rectangle
    rectangle_mask = np.zeros_like(frame, dtype=np.uint8)
    cv2.rectangle(rectangle_mask, (x, y), (x + rectangle_width, y + rectangle_height), (255, 255, 255), -1)

    # Apply the rectangle mask to the frame
    inside_rect = cv2.bitwise_and(frame, rectangle_mask)

    # Darken the area outside the rectangle
    alpha = 0.3  # You can adjust this value to control the transparency
    outside_rect = cv2.addWeighted(frame, 1 - alpha, inside_rect, alpha, 0)

    # Resize the frame for display
    display_frame = cv2.resize(outside_rect, (video_width, video_height))

    # Display the resulting frame
    cv2.imshow('Camera', display_frame)

    # Check if it's time to capture an image
    current_time = time.time()
    if current_time - last_capture_time >= capture_interval:
        # Save the image
        image_filename = f'captured_image_{int(current_time)}.jpg'
        cv2.imwrite(image_filename, frame)
        print(f"Image captured and saved as '{image_filename}'")
        last_capture_time = current_time


    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
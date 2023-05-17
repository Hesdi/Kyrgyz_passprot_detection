import cv2
import numpy as np

# Define the dimensions of the rectangle
rectangle_width = 400
rectangle_height = 300

# Initialize the camera
camera = cv2.VideoCapture(0)

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

    # Display the resulting frame
    cv2.imshow('Camera', outside_rect)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()

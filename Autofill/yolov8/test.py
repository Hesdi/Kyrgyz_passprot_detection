from ultralytics import YOLO
import cv2
import numpy as np
import rec  # Import the rec module

if __name__ == '__main__':
    # Load a model
    model = YOLO("Autofill/runs/detect/train6/weights/best.pt")

    # Open the video capture
    video_capture = cv2.VideoCapture(0)  # Replace 'path_to_video.mp4' with the actual path

    # Define variables for class counting
    class_count = 0

    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()

        # Check if the frame was read successfully
        if not ret:
            break

        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Use the model to predict on the frame
        results = model(frame_rgb)

        # Get the captured image from the rec module
        captured_image = rec.captured_image

        # Check if the captured image is available
        if captured_image is not None:
            # Convert the captured image to RGB format
            captured_image_rgb = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)

            # Use the model to predict on the captured image
            captured_image_results = model(captured_image_rgb)

            # Get the class labels and scores from the captured image results
            labels = captured_image_results.xyxy[0][:, -1]
            scores = captured_image_results.xyxy[0][:, -2]

            # Count the number of unique classes with scores above a threshold
            unique_classes = np.unique(labels)
            num_classes = len(unique_classes)
            num_above_threshold = np.sum(scores > 0.5)  # Adjust the threshold as needed

            # Check if at least 8 classes are detected with scores above the threshold
            if num_classes >= 8 and num_above_threshold >= 8:
                # Save the captured image with the predicted bounding boxes
                captured_image_results.save(save_dir='Autofill/images/results')

                # Exit the loop and end the program
                break

        # Process the prediction results on the video frame
        # ...

        # Display the frame with the prediction results
        # ...

        # Check for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close the windows
    video_capture.release()
    cv2.destroyAllWindows()

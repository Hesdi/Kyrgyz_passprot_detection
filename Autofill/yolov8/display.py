import cv2

def display_captured_image(captured_image_queue, finish_event):
    while True:
        # Get the captured image from the queue
        captured_image = captured_image_queue.get()

        # Display the captured image
        cv2.imshow('Captured Image', captured_image)

        # Check for the 'b' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('b'):
            break

        # Check if the display_frame process has finished
        if finish_event.is_set():
            break

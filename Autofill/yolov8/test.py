import cv2
import numpy as np
import onnxruntime as ort
import tensorflow as tf

# Load the ONNX model
model_path = 'C:/Users/abdul/Documents/.Prog/MachineLearning/runs/detect/train8/weights/best.onnx'
sess = ort.InferenceSession(model_path)
input_name = sess.get_inputs()[0].name
output_name = sess.get_outputs()[0].name

# Define the object classes
class_names = ['ID_cards']

# Set up the webcam
cap = cv2.VideoCapture(0)

def postprocess(output):
    num_classes = 80
    confidence_threshold = 0.5
    iou_threshold = 0.4

    anchors = np.array([12, 16, 19, 36, 40, 28, 36, 75, 76, 55, 72, 146, 142, 110, 192, 243, 459, 401]).reshape(-1, 2)

    grid_size = 80
    num_anchors = 3

    # Reshape output to grid size x grid size x num anchors x (num classes + 5)
    output = output.reshape((1, num_anchors, -1, num_classes + 5))

    # Get bounding box information from output
    boxes = output[:, :, :, :4]
    box_centers = boxes[:, :, :, :2]
    box_sizes = boxes[:, :, :, 2:4]

    # Adjust box coordinates using anchor boxes
    anchors = anchors.reshape(1, num_anchors, 1, 2)
    box_centers = box_centers * 2.0 - 0.5
    box_sizes = np.exp(box_sizes) * anchors

    # Convert box coordinates to top-left and bottom-right
    boxes = np.concatenate([box_centers - box_sizes / 2, box_centers + box_sizes / 2], axis=-1)

    # Get confidence scores and class probabilities from output
    confidence_scores = output[:, :, :, 4:5]
    class_probabilities = output[:, :, :, 5:]

    # Get class predictions
    class_predictions = np.argmax(class_probabilities, axis=-1)

    # Filter out boxes with low confidence scores
    mask = confidence_scores >= confidence_threshold
    boxes = boxes[mask]
    class_predictions = class_predictions[mask]
    confidence_scores = confidence_scores[mask]

    # Apply non-maximum suppression to filter out overlapping boxes
    selected_indices = tf.image.non_max_suppression(
        boxes=boxes,
        scores=tf.squeeze(confidence_scores),
        max_output_size=100,
        iou_threshold=iou_threshold,
        score_threshold=confidence_threshold
    )

    # Gather selected boxes, labels, and scores
    boxes = tf.gather(boxes, selected_indices).numpy()
    labels = tf.gather(class_predictions, selected_indices).numpy()
    scores = tf.gather(tf.squeeze(confidence_scores), selected_indices).numpy()

    return boxes, labels, scores


while True:
    # Read the frame from the webcam
    ret, frame = cap.read()
    
    # Preprocess the input frame
    resized_frame = cv2.resize(frame, (640, 640))
    input_data = resized_frame.transpose((2, 0, 1)).astype(np.float32)
    input_data = np.expand_dims(input_data, axis=0)
    
    # Run inference on the model
    output = sess.run([output_name], {input_name: input_data})[0]

    
    # Postprocess the model output
    boxes, labels, scores = postprocess(output)
    
    # Draw the bounding boxes on the frame
    for box, label, score in zip(boxes, labels, scores):
        x1, y1, x2, y2 = box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{class_names[label]} {score:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
    # Show the output frame
    cv2.imshow('Object Detection', frame)
    
    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
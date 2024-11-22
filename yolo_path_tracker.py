import cv2
import numpy as np
from tracker import Tracker


# Load YOLO model
net = cv2.dnn.readNetFromDarknet("yolo_files/yolov3.cfg","yolo_files/yolov3.weights")
yolo_layers = ['yolo_82', 'yolo_94', 'yolo_106']

# Load video
video_path = 'input.webm'
cap = cv2.VideoCapture(video_path)

# Initialize the tracker
tracker = Tracker()

# Determine the total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Set up the video writer for output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For MP4 format
out_vid = cv2.VideoWriter('output.mp4', fourcc, 15.0, (int(cap.get(3)), int(cap.get(4))))

# Process each frame
for _ in range(total_frames):
    ret, frame = cap.read()
    if not ret:
        break

    # - Convert frame to blob
    # - Use YOLO net to detect objects
    # - Apply Non-Maximum Suppression (NMS) to filter out overlapping boxes
    # - Update the tracker with the centroids of detected objects
    # - Draw bounding boxes, trails, and labels on the frame

    # Write the processed frame to the output video
    out_vid.write(frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video writer and video capture objects
out_vid.release()
cap.release()
cv2.destroyAllWindows()

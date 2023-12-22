## Introduction
Looking for a way to speed document checking procedures in government services in Kyrgyzstan. An AI module trained to detect national ID cards and exctract data from them using EasyOCR. The model was trained using yolov8 pre-trained and database of 400 ID card photos labeled using Label Studio.


## Features

### 1. Ultralytics YoloV8

![](yolov8.jpg)

Ultralytics YOLOv8 is a cutting-edge, state-of-the-art (SOTA) model that builds upon the success of previous YOLO versions and introduces new features and improvements to further boost performance and flexibility. YOLOv8 is designed to be fast, accurate, and easy to use, making it an excellent choice for a wide range of object detection and tracking, instance segmentation, image classification and pose estimation tasks.

### 2. Label Studio

![](labelstd.jpg)

Label Studio is an open source data labeling tool. It lets you label data types like audio, text, images, videos, and time series with a simple and straightforward UI and export to various model formats. It can be used to prepare raw data or improve existing training data to get more accurate ML models.

### 3. EasyOCR

Ready-to-use OCR with 80+ supported languages and all popular writing scripts including: Latin, Chinese, Arabic, Devanagari, Cyrillic, etc.


## Getting Started

### Autofill
Clone this directory if you want to train your model.
- /yolov8/usage.py  train model here
- /yolov8/test.py   test your model using camera
- /yolov8/test1.py  download relevant images for testing

### Final/Autofill_fin
Clone this directory if you want to test best trained model.
- /best.pt          the model you want to use
- /create_images.py cut the image into parts for detection
- /read_images.py   process the cut images and read data
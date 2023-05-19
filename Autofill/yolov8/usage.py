from ultralytics import YOLO
import numpy as np

if __name__ == '__main__':
    # Load a model
    model = YOLO("C:/Users/abdul/Documents/.Prog/Course2/Autofill/runs/detect/train6/weights/best.pt")
    # model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # # Use the model
    # model.train(data="Autofill/mydataset.yaml", epochs=1000)  # train the model
    captured_image_results = model.predict(source=0, show=True, save_crop=True, conf=0.5) #predict on an image

    # metrics = model.val()  # evaluate model performance on the validation set
    # results = model("C:/Users/abdul/Documents/.Prog/MachineLearning/1662379777704.jpg")  # predict on an image
    # success = model.export(format="onnx")  # export the model to ONNX format
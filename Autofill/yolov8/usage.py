from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model
    model = YOLO("C:/Users/abdul/Documents/.Prog/Course2/Autofill/runs/detect/train8/weights/best.pt")
    # model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

    # # Use the model
    model.train(data="Autofill/mydataset.yaml", epochs=100)  # train the model
    model.predict(source='C:/Users/abdul/Documents/.Prog/MachineLearning/1662379777704.jpg', show=True, save=True, conf=0.5) #predict on an image
    # metrics = model.val()  # evaluate model performance on the validation set
    # results = model("C:/Users/abdul/Documents/.Prog/MachineLearning/1662379777704.jpg")  # predict on an image
    # success = model.export(format="onnx")  # export the model to ONNX format
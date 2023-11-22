# from ultralytics import YOLO

# # Load a model
# model = YOLO('yolov8n-cls.yaml')  # build a new model from YAML
# model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# # Train the model
# results = model.train(data='the_palm_killer-2', epochs=100, imgsz=64)

from roboflow import Roboflow
rf = Roboflow(api_key="IlGXEoFFKWJTkBTDU7Pp")
project = rf.workspace("cmkl").project("the_palm_killer")
dataset = project.version(4).download("yolov5")

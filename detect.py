# from roboflow import Roboflow
# rf = Roboflow(api_key="IlGXEoFFKWJTkBTDU7Pp")
# project = rf.workspace("cmkl").project("the_palm_killer")
# dataset = project.version(3).download("yolov8")


# online dataset

# from roboflow import Roboflow
# rf = Roboflow(api_key="IlGXEoFFKWJTkBTDU7Pp")
# project = rf.workspace("palm-fruit-classification").project("palm-fruit-ripeness-classificationcnn")
# dataset = project.version(3).download("folder")


# from roboflow import Roboflow
# rf = Roboflow(api_key="IlGXEoFFKWJTkBTDU7Pp")
# project = rf.workspace("malam-present-lroit").project("image-detection-d4en0")
# dataset = project.version(1).download("yolov8")


# from roboflow import Roboflow
# rf = Roboflow(api_key="IlGXEoFFKWJTkBTDU7Pp")
# project = rf.workspace("usim-8qwft").project("image-classification-and-fruit-counting-of-oil-palm-fruit-bunches-cvuc1")
# dataset = project.version(1).download("yolov8")


# from roboflow import Roboflow
# rf = Roboflow(api_key="IlGXEoFFKWJTkBTDU7Pp")
# project = rf.workspace("deteksi-objek-tbs").project("kematangan-tbs-sawit")
# dataset = project.version(7).download("yolov8")


from roboflow import Roboflow
rf = Roboflow(api_key="IlGXEoFFKWJTkBTDU7Pp")
project = rf.workspace("1171102868").project("ffb-oil-plamv2")
dataset = project.version(1).download("yolov8")


from roboflow import Roboflow

rf = Roboflow(api_key="IlGXEoFFKWJTkBTDU7Pp")
project = rf.workspace("cmkl").project("the_palm_killer")
dataset = project.version(1).download("yolov7")

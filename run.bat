@REM @echo off
@REM set KMP_DUPLICATE_LIB_OK=TRUE
@REM set COMET_API_KEY=yS2kapxkbW9MspfL36jVnngGu
@REM set COMET_PROJECT_NAME=the-palm-killer-4
@REM yolo detect train data=the_palm_killer-4/data.yaml model=yolov5n.yaml epochs=100 imgsz=640 batch=64
yolo detect predict model=runs\detect\train3\weights\best.pt source='6_2.jpg'
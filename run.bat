@REM @echo off
@REM set KMP_DUPLICATE_LIB_OK=TRUE
@REM set COMET_API_KEY=yS2kapxkbW9MspfL36jVnngGu
@REM set COMET_PROJECT_NAME=the-palm-killer-5
@REM yolo detect train data=data.yaml model=yolov5n.yaml epochs=200 imgsz=640
yolo detect predict model=train_apex_1/weights/best.pt source='6_2.jpg'
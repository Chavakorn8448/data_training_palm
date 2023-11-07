@REM @echo off
@REM set KMP_DUPLICATE_LIB_OK=TRUE
@REM set COMET_API_KEY=yS2kapxkbW9MspfL36jVnngGu
@REM set COMET_PROJECT_NAME=the-palm-killer
@REM yolo detect train data=data.yaml model=yolov8n.yaml epochs=100 imgsz=640 batch=64
yolo detect predict model=runs\detect\train\weights\best.pt source='222_3.jpg'

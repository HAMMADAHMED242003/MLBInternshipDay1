# Object Detection using YOLOv8

## What is Object Detection?

Object Detection is a computer vision task that finds objects in an image and draws bounding boxes around them. It also tells what the object is.

## How is it different from Image Classification?

Image Classification gives one label for the whole image. Object Detection can find multiple objects and show their locations.

## What is YOLO?

YOLO (You Only Look Once) is a fast object detection model. It detects objects, predicts their classes, and draws bounding boxes in one step.

## Which dataset did you use?

I used a Coco128 dataset in YOLO format.

## What objects were detected?

The model detected objects like persons, tv objects and animals.

## Observations about the detection results

The model detected mostly correctly and generated bounding boxes with confidence scores. Some small or unclear objects were missed or detected with lower confidence because I used a pre-trained model without training it on this dataset.
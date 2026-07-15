# Cats vs Dogs Image Classifier using Transfer Learning

## What is Transfer Learning

Transfer Learning is a technique where a model that has already been trained on a large dataset is reused for a new task. Instead of training a model from scratch, it uses the knowledge it has already learned to improve accuracy and reduce training time.

## Why I Chose MobileNetV2

I chose MobileNetV2 because it is lightweight, fast, and provides high accuracy. It is pre-trained on the ImageNet dataset and works well for image classification while requiring less computational power.

## Experiments Performed

To improve the model performance I resized all images to 224 × 224, normalized the pixel values, froze the MobileNetV2 base model, added custom classification layers, and trained the model for 5 epochs using the Adam optimizer.

## Final Validation Accuracy

The model achieved a final validation accuracy of **98.39%** with the best validation accuracy of **98.62%**.

## Challenges and Lessons Learned

The main challenge was understanding how transfer learning works and how freezing the base model affects training. I also learned how to preprocess image data, build a custom classification head, and evaluate the model using accuracy and loss graphs. This project showed me that transfer learning can achieve excellent results without training a CNN from scratch.
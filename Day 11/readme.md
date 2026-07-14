
## Why CNNs are Better than ANNs

CNNs are better for image data because they automatically learn important features like edges, shapes, and textures using convolution layers. Unlike ANNs, CNNs preserve the spatial relationship between pixels and require fewer parameters, resulting in better accuracy.

## Purpose of Convolution and Pooling Layers
Convolution Layer: Extracts important features such as edges and patterns from images.
Pooling Layer: Reduces the size of feature maps, speeds up training, and helps prevent overfitting.

## Model Architecture
    Input Layer (28×28×1)
    Conv2D (32 filters, ReLU)
    MaxPooling2D
    Conv2D (64 filters, ReLU)
    MaxPooling2D
    Flatten
    Dense (128, ReLU)
    Dropout (0.5)
    Output Layer (10 classes, Softmax)
## Results
    Training Accuracy: 91%
    Validation Accuracy: 89%
    Testing Accuracy: 91%

The model performed well, and the confusion matrix showed that most predictions were correct. Some confusion occurred between similar clothing items like Shirt, T-shirt, Pullover, and Coat.

## Challenges Faced
Understanding how CNN differs from ANN.
Reshaping images to the correct input shape.
Converting prediction probabilities into class labels using np.argmax().
Creating and interpreting the confusion matrix.
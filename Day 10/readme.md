# Deep Learning – Day 10

## What is Deep Learning?

Deep Learning is a branch of Machine Learning that uses Artificial Neural Networks (ANNs) with multiple hidden layers to automatically learn complex patterns from data. Unlike traditional Machine Learning, Deep Learning can extract features directly from raw data, making it highly effective for tasks such as image classification, object detection, speech recognition, natural language processing, and autonomous driving.


## Difference Between Machine Learning and Deep Learning

Machine Learning often requires manual feature engineering, where the developer selects the important features from the data before training the model. In contrast, Deep Learning automatically learns these features through multiple neural network layers.

Machine Learning generally performs well on small to medium-sized datasets and requires less computational power. Deep Learning, however, usually needs large datasets and high-performance hardware such as GPUs to train effectively.

Traditional Machine Learning algorithms include Linear Regression, Logistic Regression, Decision Trees, and Support Vector Machines (SVM). Deep Learning relies on deep neural networks with multiple hidden layers to learn complex relationships within the data.

Machine Learning is commonly used for structured or tabular data, whereas Deep Learning excels at processing unstructured data such as images, audio, and text.



## What is a Perceptron?

A Perceptron is the fundamental building block of an Artificial Neural Network. It receives multiple input values, multiplies each input by a corresponding weight, adds a bias, and then applies an activation function to produce the final output.

Mathematically, a perceptron computes:

z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b

The calculated value is then passed through an activation function, which determines the output of the neuron.


## Activation Functions Explored

### ReLU (Rectified Linear Unit)

ReLU returns the input value if it is positive; otherwise, it returns zero. It is the most commonly used activation function in the hidden layers of deep neural networks because it introduces non-linearity, speeds up training, and helps mitigate the vanishing gradient problem.

### Sigmoid

The Sigmoid activation function produces output values between 0 and 1. It is mainly used in the output layer of binary classification models where the prediction represents a probability.

### Tanh

Tanh produces output values between -1 and 1. Since its outputs are centered around zero, it can perform better than Sigmoid in some hidden-layer scenarios.

### Softmax

Softmax converts the outputs of the final layer into probabilities whose sum equals 1. It is commonly used in the output layer of multi-class classification problems, such as the Fashion MNIST dataset, where the model predicts one class among multiple categories.

## Model Performance

After training the Artificial Neural Network on the Fashion MNIST dataset, the model achieved:

Training Accuracy:90.86%
Validation Accuracy:88.39%
Testing Accuracy:87.48%
Testing loss:0.3568

## Conclusion

Today, I gained a solid understanding of Deep Learning fundamentals, including Artificial Neural Networks, perceptrons, and activation functions. I also built my first ANN using TensorFlow/Keras, trained it on the Fashion MNIST dataset, evaluated its performance, and learned how to make predictions on unseen images.

# Document Image Enhancement Tool

## Overview

This project is a Document Image Enhancement Tool developed using Python and OpenCV. The main goal of the project is to improve the quality of document images by applying different image processing techniques. The application can correct tilted documents, reduce noise, improve brightness and contrast, sharpen the image, and save the final enhanced result.

## Transformations Implemented

### Perspective Transformation

Perspective transformation was used to straighten tilted document images. It detects the four corners of the document and transforms the image into a top-down view, making it look like a properly scanned document.

### Grayscale Conversion

The document was converted from a colored image to grayscale. This removes unnecessary color information and makes further image processing faster and more effective.

### Noise Reduction

A bilateral filter was applied to reduce image noise while preserving the edges of the text. This helps produce a cleaner document without blurring important details.

### Brightness and Contrast Enhancement

Brightness and contrast were adjusted using OpenCV to make the document clearer and improve the visibility of the text, especially in faded or low-quality images.

### Image Sharpening

A sharpening filter was applied to make the text edges more defined. This improves the overall readability of the document.



## Purpose of Each Enhancement Technique

Each enhancement technique was applied to improve a different aspect of the document image. Grayscale conversion simplified the image for processing, while noise reduction removed unwanted distortions without affecting the text. Brightness and contrast adjustments made the document easier to read by improving the visibility of the content. Finally, sharpening enhanced the text edges, making the document appear clearer and more readable.


## Which Transformation Had the Biggest Impact?

Among all the techniques, perspective transformation had the biggest impact on the document quality. It converted tilted document images into properly aligned documents, making the text easier to read and improving the effectiveness of the remaining enhancement techniques.


## Challenges Faced During Implementation

One of the main challenges was detecting the correct document boundary. Some images contained diagrams or figures that were detected as the document instead of the page itself. Another challenge was selecting suitable values for brightness, contrast, and sharpening so that the image quality improved without introducing unwanted artifacts. It also took some experimentation to generate realistic tilted document images for testing the perspective correction algorithm.


## Conclusion

This project successfully demonstrates how image processing techniques can be combined to improve the quality of document images. The implemented pipeline can straighten tilted documents, enhance their appearance, and produce cleaner images that are more suitable for reading or OCR applications.
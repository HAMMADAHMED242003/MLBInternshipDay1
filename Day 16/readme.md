# Document Image Processing and Boundary Detection

## Overview

This project focuses on improving document image quality and detecting document boundaries using different image processing techniques in OpenCV. The implemented methods include edge detection algorithms and morphological operations to enhance document structures before further analysis.


## Edge Detection Techniques

### Sobel Edge Detection

Sobel detects edges by calculating the gradient of image intensity in horizontal and vertical directions.

- Detects changes in brightness along the X and Y axes.
- Provides information about edge direction.
- Less sensitive to noise compared to simple gradient methods.
- Useful for detecting strong document edges.

### Laplacian Edge Detection

Laplacian detects edges by calculating the second derivative of image intensity.

- Detects rapid changes in pixel intensity.
- Detects edges in all directions.
- More sensitive to noise, so smoothing is often applied before using it.
- Useful for highlighting fine details and sharp boundaries.

### Canny Edge Detection

Canny is an advanced multi-stage edge detection algorithm.

Steps involved:
1. Noise reduction using Gaussian filtering.
2. Gradient calculation.
3. Non-maximum suppression to refine edges.
4. Double thresholding and edge tracking.

Advantages:
- Produces thin and accurate edges.
- Removes many unwanted edges.
- Works well for document boundary detection.


## Morphological Operations

Morphological operations are used to process binary images and improve the quality of detected document regions.

### Erosion

- Removes small white regions and noise.
- Helps eliminate unwanted small objects from the image.
- Can make thin text regions smaller.

### Dilation

- Expands white regions.
- Connects broken edges and text regions.
- Helps strengthen detected document boundaries.

### Opening

- Combination of erosion followed by dilation.
- Removes small noise while preserving important structures.
- Useful for cleaning binary document images.

### Closing

- Combination of dilation followed by erosion.
- Fills small holes and gaps in detected regions.
- Helps connect broken document boundaries.



## Best Performing Combination

The combination that produced the best results was:

**Gaussian Blur + Canny Edge Detection + Morphological Closing**

Reasons:

- Gaussian Blur reduced noise before edge detection.
- Canny generated clear and accurate document boundary edges.
- Morphological Closing connected broken edges and filled small gaps.

This combination produced cleaner document contours and improved boundary detection compared to using individual techniques alone.



## Challenges Faced During Document Boundary Detection

### 1. Uneven Lighting Conditions
Some document images contained shadows and different brightness levels, which affected edge detection.

**Solution:**
Applied grayscale conversion, Gaussian filtering, and thresholding techniques.

### 2. Background Noise
Unwanted objects and noise sometimes created false edges.

**Solution:**
Used morphological operations to remove noise and improve edge quality.

### 3. Broken Document Edges
Some document boundaries were incomplete due to low contrast or image quality.

**Solution:**
Applied morphological closing and dilation to connect broken edges.

### 4. Selecting Proper Parameters
Choosing suitable threshold values and kernel sizes required experimentation.

**Solution:**
Tested different parameter combinations to achieve better document boundary detection.


## Conclusion

This project demonstrates how edge detection and morphological processing techniques can improve document boundary detection. Among the tested approaches, the combination of Canny Edge Detection with morphological closing provided the most reliable results by producing clearer and more connected document edges.
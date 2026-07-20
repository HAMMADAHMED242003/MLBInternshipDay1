# Image Processing Toolkit using OpenCV

## Overview

This project is a menu-driven Python application built using OpenCV. It allows users to perform basic image processing operations such as loading an image, converting it to grayscale, resizing, cropping, rotating, flipping, drawing shapes, adding text, and saving the processed image.



## Difference Between BGR and RGB

Both BGR and RGB are color models used to represent color images. The difference lies in the order of the color channels.

### RGB (Red, Green, Blue)

- RGB stores colors in the order:
  - Red
  - Green
  - Blue
- It is the standard color format used by most image processing libraries and display systems such as Matplotlib and web browsers.

Example:

  python
(255, 0, 0)


In RGB, this represents **Red**.

### BGR (Blue, Green, Red)

- OpenCV uses the BGR color format by default.
- The channel order is:
  - Blue
  - Green
  - Red

Example:

python
(255, 0, 0)


In OpenCV (BGR), this represents **Blue**, not red.

### Why Convert BGR to RGB?

When displaying an OpenCV image using Matplotlib, the image must first be converted from BGR to RGB; otherwise, the colors will appear incorrect.

Example:
python
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)




## What are Grayscale Images?

A grayscale image contains only intensity (brightness) information instead of color information.

Unlike a color image, which has three channels (Blue, Green, and Red), a grayscale image has only one channel.

Color Image:


(height, width, 3)


Grayscale Image:


(height, width)


Each pixel stores a value between:

- 0 → Black
- 255 → White
- Values between 0 and 255 represent different shades of gray.

### Why are Grayscale Images Used?

Grayscale images are commonly used because they:

- Reduce memory usage.
- Require less computation.
- Simplify image processing algorithms.
- Improve processing speed.
- Are sufficient for many computer vision tasks such as edge detection, thresholding, and feature extraction.

Example:

python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)




## OpenCV Functions Used

The following OpenCV functions were used in this project:

| Function | Purpose |

| `cv2.imread()`  Load an image |
| `cv2.imshow()`  Display an image |
| `cv2.waitKey()`  Wait for a key press |
| `cv2.destroyAllWindows()` | Close image windows |
| `cv2.imwrite()` Save an image |
| `cv2.cvtColor()`  Convert color spaces (BGR to RGB, BGR to Grayscale) |
| `cv2.resize()`  Resize an image |
| `cv2.rotate()`  Rotate an image |
| `cv2.flip()`  Flip an image horizontally or vertically |
| `cv2.rectangle()`  Draw a rectangle |
| `cv2.circle()` Draw a circle |
| `cv2.line()`  Draw a line |
| `cv2.polylines()`  Draw a polygon |
| `cv2.putText()` Add text to an image |



## Challenges Faced and Solutions

### 1. Incorrect Colors While Displaying Images

**Challenge:**
Images displayed using Matplotlib showed incorrect colors.

**Solution:**
Converted images from BGR to RGB before displaying.

python
cv2.cvtColor(image, cv2.COLOR_BGR2RGB)




### 2. Understanding Image Coordinates

**Challenge:**
Initially, it was confusing whether coordinates represented rows or columns.

**Solution:**
Learned that:

- X represents the column (width).
- Y represents the row (height).

Image indexing follows:

python
image[y, x]


### 3. Polygon Going Outside the Image

**Challenge:**
Some polygon points were outside the image boundaries.

**Solution:**
Checked the image dimensions using:

python
image.shape


Then adjusted the polygon coordinates so all points remained inside the image.



### 4. Saving Images

**Challenge:**
Saving images failed when the output folder did not exist.

**Solution:**
Created the folder before saving.

python
os.makedirs("output", exist_ok=True)



### 5. Displaying Images in Kaggle

**Challenge:**
`cv2.imshow()` does not work in Kaggle notebooks.

**Solution:**
Used Matplotlib to display images.

python
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()



## Conclusion

This project helped build a strong understanding of OpenCV fundamentals and basic image processing operations. It provided practical experience with image manipulation techniques that serve as the foundation for advanced computer vision tasks such as object detection, image segmentation, and facial recognition.
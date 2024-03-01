import cv2
import pandas as pd
import numpy as np

image = cv2.imread("atrial.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Set threshold level
threshold_level = 50

# Create mask of all pixels lower than threshold level
mask = gray < threshold_level

# Color the pixels in the mask
image[mask] = (255, 255, 255)
image[~mask] = (0,0,0)

white_pixels = np.where(image == 255)
animated_image = np.zeros_like(image)
chunk_size = 100


for i in range(0, len(white_pixels[0]), chunk_size):  # Iterate over rows
    chunk_rows = white_pixels[0][i:i+chunk_size]
    chunk_cols = white_pixels[1][i:i+chunk_size]
    for y, x in zip(chunk_rows, chunk_cols):  # Combine and iterate over coordinates
        if 0 <= x < animated_image.shape[1] and 0 <= y < animated_image.shape[0]:
            animated_image[y, x] = 255  # Set selected pixels to white
    animated_image = cv2.convertScaleAbs(animated_image, alpha=(255.0/animated_image.max()))
    cv2.imshow('image', animated_image)
    cv2.waitKey(1)

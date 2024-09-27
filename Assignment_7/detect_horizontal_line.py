import cv2
import numpy as np

image = cv2.imread('/Users/likithgannarapu/Desktop/MU/7 Sem/AI in Industry/Assignment_7/test.png', cv2.IMREAD_GRAYSCALE)

kernel = np.array([[-1, -1, -1],
                   [ 2,  2,  2],
                   [-1, -1, -1]])

horizontal_edges = cv2.filter2D(image, -1, kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Horizontal Edges', horizontal_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

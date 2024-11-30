import cv2
import numpy as np

def preprocess_image(path, resize_format = (28,28)):
    img = cv2.imread(path)
    img_resized = cv2.resize(img, resize_format)
    return img_resized
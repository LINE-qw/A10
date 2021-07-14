import os
from loader.config import *
import cv2

#加载图片
def loadImages():
    images = []
    image_names = os.listdir(r"./" + IMAGES_PATH)
    for image_name in image_names:
        image_path = os.path.join(IMAGES_PATH, image_name)
        image = cv2.imread(image_path)
        images.append(image)
    return images

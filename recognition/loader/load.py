import os
from loader.config import *
import cv2


# 加载图片集（李奇伟 2021.07.9）
def loadImages():
    images = []
    image_names = os.listdir(r"./" + IMAGES_PATH)
    for image_name in image_names:
        image_path = os.path.join(IMAGES_PATH, image_name)
        image = cv2.imread(image_path)
        images.append(image)
    return images


# 获取Excel文件路径（李奇伟 2021.07.16）
def getExcelFilePath(file_name):
    excelfile_path = os.path.join(EXCELFILE_PATH, file_name)
    return excelfile_path


# 获取Excel文件夹路径（李奇伟 2021.07.16）
def getExcelDectionaryPath():
    return EXCELFILE_PATH


def getExcelFileAbsPath(file_name):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    excelfiles_path = os.path.join(dir_path,'excelfiles')
    excelfile_path = os.path.join(excelfiles_path,file_name)
    return excelfile_path


# 加载图片（李奇伟 2021.07.16）
def loadImage(image_name):
    image_path = os.path.join(IMAGES_PATH, image_name)
    image = cv2.imread(image_path)
    return image


# 获取图片路径（李奇伟 2021.07.16）
def getImagePath(image_name):
    image_path = os.path.join(IMAGES_PATH, image_name)
    return image_path


# 清空图片文件夹（李奇伟 2021.07.16）
def emptyImages():
    image_names = os.listdir(r"./" + IMAGES_PATH)
    for image_name in image_names:
        image_path = os.path.join(IMAGES_PATH, image_name)
        os.remove(image_path)


# 清空Excel文件夹（李奇伟 2021.07.16）
def emptyExcels():
    excelfiles_names = os.listdir(r"./" + EXCELFILE_PATH)
    for excelfile_name in excelfiles_names:
        excelfile_path = os.path.join(EXCELFILE_PATH, excelfile_name)
        os.remove(excelfile_path)

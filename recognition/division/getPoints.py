#（李奇伟 2021.07.10）
import cv2
import numpy as np
from division.config import *


# 获取图像中疑似的边框点
def getImagePoints(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 二值化
    binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)


    rows, cols = binary.shape
    scale = 40
    # 自适应获取核值
    # 识别横线:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cols // scale, 1))
    eroded = cv2.erode(binary, kernel, iterations=1)
    dilated_col = cv2.dilate(eroded, kernel, iterations=2)
    dilated_col2 = cv2.dilate(eroded, kernel, iterations=1)

    # 识别竖线：
    scale = 20
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows // scale))
    eroded = cv2.erode(binary, kernel, iterations=1)
    dilated_row = cv2.dilate(eroded, kernel, iterations=2)
    dilated_row2 = cv2.dilate(eroded, kernel, iterations=1)

    # 将识别出来的横竖线合起来
    bitwise_and = cv2.bitwise_and(dilated_col, dilated_row)

    # 标识表格轮廓
    merge = cv2.add(dilated_col, dilated_row)


    # 将焦点标识取出来
    ys, xs = np.where(bitwise_and > 0)

    return xs, ys, dilated_col2, dilated_row2


# 对边框点进行过滤
def pointFilter(xs, ys):
    points = []
    for i in range(len(ys)):
        if i + 1 < len(xs) and abs(xs[i] - xs[i + 1]) < 10:
            continue
        j = 0
        abandon = False
        while True:
            j = j + 1
            if i + j == len(ys):
                break
            if ys[i + j] - ys[i] > 10:
                break
            if ys[i + j] - ys[i] < 10 and abs(xs[i + j] - xs[i]) < 10:
                abandon = True
                break
        if abandon:
            continue
        points.append(TPoint(xs[i], ys[i]))

    return points


def processImage(points, image):
    xt = []
    yt = []
    for point in points:
        xt.append(point.x)
        yt.append(point.y)
    x_min = min(xt)
    x_max = max(xt)
    y_min = min(yt)
    y_max = max(yt)
    img = image.copy()
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 0, 0), 1)
    return img

# 获取输出结果
def getResult(image):
    xs, ys, image_col, image_row = getImagePoints(image)
    points = pointFilter(xs, ys)
    img = processImage(points, image)
    xs, ys, p_image_col, p_image_row = getImagePoints(img)
    p_points = pointFilter(xs, ys)
    return p_points, p_image_col, p_image_row

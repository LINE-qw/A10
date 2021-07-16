#（李奇伟 2021.07.12）
import cv2
import numpy as np

#聚焦图片
def focusImage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, 0)
    binary[0] = 255
    binary[-1] = 255
    binary[:, 0] = 255
    binary[:, -1] = 255
    row_sum = getRowSum(binary)
    imgs = getTextBox(image, row_sum, binary)
    return imgs

#获取行统计数组
def getRowSum(binary):
    row_num = binary.shape[0]
    col_num = binary.shape[1]
    row_sum = np.zeros(row_num)
    col_sum = np.zeros(col_num)
    for i in range(row_num):
        for j in range(col_num):
            if binary[i][j] < 127:
                row_sum[i] = row_sum[i] + 1
    for j in range(col_num):
        for i in range(row_num):
            if binary[i][j] < 127:
                col_sum[j] = col_sum[j] + 1
    return row_sum

#获取文本框
def getTextBox(image, row_sum, binary):
    row_num = binary.shape[0]
    col_num = binary.shape[1]

    i1 = []
    i2 = []

    i = 0
    is_i1 = True
    while i < row_num:
        if is_i1:
            if row_sum[i] > 0:
                i1.append(i)
                is_i1 = False
        else:
            if row_sum[i] == 0:
                i2.append(i)
                is_i1 = True
        i = i + 1

    j1 = []
    j2 = []

    for index in range(len(i1)):
        col_sum = np.zeros(col_num)
        for j in range(col_num):
            l = i2[index] - i1[index]
            for i in range(l):
                i = i + i1[index]
                if binary[i][j] < 127:
                    col_sum[j] = col_sum[j] + 1
        j1_index = 0
        while col_sum[j1_index] == 0:
            j1_index = j1_index + 1
            if j1_index == col_num - 1:
                break
        j1.append(j1_index)
        j2_index = col_num - 1
        while col_sum[j2_index] == 0:
            j2_index = j2_index - 1
            if j2_index == 0:
                break
        j2.append(j2_index)
    images = []
    if len(i1) == 0:
        images.append(image)
        return images
    for index in range(len(i1)):
        images.append(image[i1[index] - 2: i2[index] + 2, j1[index] - 2: j2[index] + 2])
    return images

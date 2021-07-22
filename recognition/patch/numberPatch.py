# （李奇伟 2021.07.22）
import cv2
from patch.config import BIJR

#判断是否为空
def judgeBlank(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, 0)
    binary[0] = 255
    binary[-1] = 255
    binary[:, 0] = 255
    binary[:, -1] = 255
    n = 0
    for i in range(binary.shape[0]):
        for j in range(binary.shape[1]):
            if binary[i][j] == 0:
                n = n + 1
    if n/(binary.shape[0]*binary.shape[1])<BIJR:
        return True
    return False

#数字补丁
def patchNumber(image):
    if judgeBlank(image):
        return ""
    else:
        return "1"


#（李奇伟 2021.07.12）
import cv2

from division.config import *
from division.getPoints import getResult, getImagePoints

#计算边框线占比
def getCoverage(judge, p1, p2, q, line):
    n = 0
    length = p2 - p1
    if judge:
        for dl in range(length):
            if line[q, p1 + dl] > 0:
                n = n + 1
    else:
        for dl in range(length):
            if line[p1 + dl, q] > 0:
                n = n + 1
    return n / length

#获取表格边框
def getCells(image):
    cells = []
    points, image_col, image_row = getResult(image)
    for i in range(len(points) - 1):
        xl = points[i].x
        yl = points[i].y
        if abs(points[i].y - points[i + 1].y) > POINT_DIFFERENCE:
            continue
        j = 0
        k = 0
        while True:
            j = j + 1
            if i + j == len(points):
                j = -1
                break
            if points[i + j].y - points[i].y < POINT_DIFFERENCE:
                continue
            else:
                if abs(points[i].x - points[i + j].x) > POINT_DIFFERENCE:
                    continue
                qualified = False
                k = 0
                while True:
                    k = k + 1
                    if i + j + k == len(points) or points[i + j + k].y - points[i + j].y > POINT_DIFFERENCE:
                        break
                    p1 = getCoverage(True, points[i + j].x, points[i + j + k].x, points[i + j].y, image_col)
                    p2 = getCoverage(False, points[i].y, points[i + j + k].y, points[i + j + k].x, image_row)
                    if p1 > PASS_RATE and p2 > PASS_RATE:
                        qualified = True
                        break
                if qualified:
                    break
        if j == -1:
            break
        yr = points[i + j].y
        xr = points[i + j + k].x
        p3 = getCoverage(True, points[i].x, points[i + j + k].x, points[i].y, image_col)
        if p3 < PASS_RATE:
            continue
        p4 = getCoverage(False, points[i].y, points[i + j].y, points[i].x, image_row)
        if p4 < PASS_RATE:
            continue
        cells.append(TableCell(image, yl, yr, xl, xr))

    return cells

#获取表头
def getHeadCell(image):
    xs, ys, image_col, image_row = getImagePoints(image)
    head_cell = TableCell(image, 0, min(ys), min(xs), max(xs))
    return head_cell

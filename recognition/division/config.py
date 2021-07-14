
# 表格单元类（李奇伟 2021.07.10）
class TableCell:
    def __init__(self, image, yl, yr, xl, xr):
        self.xl = xl
        self.xr = xr
        self.yl = yl
        self.yr = yr
        self.cell_image = image[yl: yr, xl: xr]
        self.value = ""#单元格内容
        self.position = [0, 0, 0, 0]#左上行，左上列，右下行，右下列

    # 获取表格图像
    def getCellImage(self):
        return self.cell_image


# 表格特征点类（李奇伟 2021.07.10）
class TPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


POINT_DIFFERENCE = 10
PASS_RATE = 0.95
R_TEXT_HEIGHT = 14.63



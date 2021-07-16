
# 表格单元类（李奇伟 2021.07.10）
class TableCell:
    #初始化
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
    #初始化
    def __init__(self, x, y):
        self.x = x
        self.y = y

#不同点的区分距离
POINT_DIFFERENCE = 10
#判断满足边界框线的合格率
PASS_RATE = 0.95
#转化表格高度系数
R_TEXT_HEIGHT = 14.63



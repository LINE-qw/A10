#（李奇伟 2021.07.13）
from division import config

#表格类（李奇伟 2021.07.13）
class TableData:
    #初始化
    def __init__(self, cells, text_height):
        self.cells = cells
        self.text_height = text_height
        self.row_lines = self.getRowLine()
        self.col_lines = self.getColLine()
        self.row_num = len(self.row_lines) - 1#行数
        self.col_num = len(self.col_lines) - 1#列数
        self.setCellPositition()
        self.setTable()
        self.head_cell_texts = []#表头数组

    # 获取表格行数
    def getRowLine(self):
        y = []
        for i in range(len(self.cells)):
            if i == 0:
                y.append(self.cells[i].yl)
                continue
            in_yl = True
            in_yr = True
            for j in y:
                if abs(j - self.cells[i].yl) < config.POINT_DIFFERENCE:
                    in_yl = False
                if abs(j - self.cells[i].yr) < config.POINT_DIFFERENCE:
                    in_yr = False
            if in_yl:
                y.append(self.cells[i].yl)
            if in_yr:
                y.append(self.cells[i].yr)
        y.sort()
        return y

    # 获取表格列数
    def getColLine(self):
        x = []
        for i in range(len(self.cells)):
            if i == 0:
                x.append(self.cells[i].xl)
                continue
            in_xl = True
            in_xr = True
            for j in x:
                if abs(j - self.cells[i].xl) < config.POINT_DIFFERENCE:
                    in_xl = False
                if abs(j - self.cells[i].xr) < config.POINT_DIFFERENCE:
                    in_xr = False
            if in_xl:
                x.append(self.cells[i].xl)
            if in_xr:
                x.append(self.cells[i].xr)
        x.sort()
        return x

    #设置每个单元格位置
    def setCellPositition(self):
        row_lines = self.row_lines
        col_lines = self.col_lines
        for cell in self.cells:
            for i in range(len(row_lines)):
                if abs(cell.yl - row_lines[i]) < config.POINT_DIFFERENCE:
                    cell.position[0] = i + 1
                if abs(cell.yr - row_lines[i]) < config.POINT_DIFFERENCE:
                    cell.position[2] = i
                    continue
            for j in range(len(col_lines)):
                if abs(cell.xl - col_lines[j]) < config.POINT_DIFFERENCE:
                    cell.position[1] = j + 1
                if abs(cell.xr - col_lines[j]) < config.POINT_DIFFERENCE:
                    cell.position[3] = j
                    continue

    #设置表格行高、列宽
    def setTable(self):
        p0 = config.R_TEXT_HEIGHT/self.text_height
        col_widths = []
        row_heights = []
        for i in range(self.col_num):
            col_width = round(p0*(self.col_lines[i+1] - self.col_lines[i]))
            col_widths.append(col_width)
        for j in range(self.row_num):
            raw_height = round(p0 * (self.row_lines[j + 1] - self.row_lines[j]))
            row_heights.append(raw_height)
        self.col_widths = col_widths
        self.row_heights = row_heights
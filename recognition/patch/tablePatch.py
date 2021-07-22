# （李奇伟 2021.07.21）
from patch.config import *


# 判断是否为数字或符号
def DS(value):
    if len(value) == 0:
        return False
    for i in value:
        if '0' <= i <= '9':
            continue
        if i == '.' or i == ',' or i == '，':
            continue
        return False
    return True


# 判断是否为数字或符号或空
def DSB(value):
    for i in value:
        if '0' <= i <= '9':
            continue
        if i == '.' or i == ',' or i == '，':
            continue
        return False
    return True


# 按列划分
def getCols(cells, col_num):
    cols = []
    for i in range(col_num):
        col = []
        for cell in cells:
            if i + 1 == cell.position[1]:
                col.append(cell)
        cols.append(col)
    return cols


# 去除文字单元，保留数字单元
def getDigitalCols(cols):
    digital_cols = []
    for col in cols:
        digital_col = []
        for cell in col:
            if DSB(cell.value):
                digital_col.append(cell)
        digital_cols.append(digital_col)
    return digital_cols


# 判断小数
def decimals(col):
    if len(col) == 0:
        return 0, -1
    data = {}
    for cell in col:
        point = False
        n = 0
        for i in cell.value:
            if i == '.':
                point = True
            if point and '0' <= i <= '9':
                n = n + 1
        in_data = False
        for key in data.keys():
            if n == key:
                in_data = True
                data[key] = data[key] + 1
        if not in_data:
            data.update({n: 1})
    max_value = 0
    max_key = -1
    for key in data.keys():
        if data[key] > max_value:
            max_value = data[key]
            max_key = key
    return max_value / len(col), max_key


# 插入字符
def str_insert(str_origin, pos, str_add):
    str_list = list(str_origin)  # 字符串转list
    str_list.insert(pos, str_add)  # 在指定位置插入字符串
    str_out = ''.join(str_list)  # 空字符连接
    return str_out


# 修正单元格值
def decimalsCorrect(cells, col, digit):
    dcells = []
    for cell in col:
        if DS(cell.value):
            if cell.value[-1 - digit] != '.':
                dcells.append(cell)
    for dcell in dcells:
        for cell in cells:
            if dcell.position[0] == cell.position[0] and dcell.position[1] == cell.position[1]:
                cell.value = str_insert(cell.value, len(cell.value) - digit, '.')


# 表格后期优化
def patchUp(cells, col_num):
    cols = getCols(cells, col_num)
    cols = getDigitalCols(cols)
    for col in cols:
        drate, digit = decimals(col)
        if CDCPR < drate < 1:
            decimalsCorrect(cells, col, digit)
    return cells

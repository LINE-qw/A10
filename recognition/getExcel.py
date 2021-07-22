# （李奇伟 2021.07.15）
import xlwt


# 单元格风格
def title_style():
    # 创建字体
    font = xlwt.Font()
    # 字体类型
    font.name = '仿宋'
    # 设置字体大小
    font.height = 20 * 11

    style = xlwt.XFStyle()
    style.alignment.horz = 2
    style.alignment.wrap = 1  # 自动换行
    style.font = font  # style的字体为上面定义的字体
    return style


# 保存excel表并返还文件名称
def getXls(table,name):
    name = name + ".xls"
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('demo')

    for i in range(table.col_num):
        worksheet.col(i).width = 60 * table.col_widths[i]
    for j in range(table.row_num):
        worksheet.row(j).height_mismatch = True
        worksheet.row(j).height = 20 * table.row_heights[j]
    h = 1
    if table.head_cell_texts[0] != "":
        h = 0
        worksheet.write_merge(0, 0, 0, table.col_num - 1, label=table.head_cell_texts, style=title_style())
    for cell in table.cells:
        worksheet.write_merge(cell.position[0] - h, cell.position[2] - h, cell.position[1] - 1, cell.position[3] - 1,
                              label=cell.value, style=title_style())
    workbook.save("loader/excelfiles/" + name)
    return name


def getXlsByImageName(table, imagename):
    name = ""
    for n in range(len(imagename)):
        if imagename[n] == '.':
            break
        name = name + imagename[n]
    name = name + ".xls"
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('demo')

    for i in range(table.col_num):
        worksheet.col(i).width = 60 * table.col_widths[i]
    for j in range(table.row_num):
        worksheet.row(j).height_mismatch = True
        worksheet.row(j).height = 20 * table.row_heights[j]
    h = 1
    if len(table.head_cell_texts):
        h = 0
        worksheet.write_merge(0, 0, 0, table.col_num - 1, label=table.head_cell_texts, style=title_style())
    for cell in table.cells:
        worksheet.write_merge(cell.position[0] - h, cell.position[2] - h, cell.position[1] - 1, cell.position[3] - 1,
                              label=cell.value, style=title_style())
    workbook.save("loader/excelfiles/" + name)
    return name

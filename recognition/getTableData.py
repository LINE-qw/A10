# （李奇伟 2021.07.14）
from division.getCells import getCells, getHeadCell
from division.tableData import TableData
from loader.load import loadImages
from texter.getBox import focusImage
from texter.getText import getHeadText, getCellText


# 获取表格信息（所有）
def getTableDatas():
    images = loadImages()
    table_datas = []
    for image in images:
        cells = getCells(image)
        for cell in cells:
            imgs = focusImage(cell.getCellImage())
            cell_texts = getCellText(imgs)
            for text in cell_texts:
                cell.value = cell.value + text
        text_height = focusImage(cells[0].getCellImage())[0].shape[0]
        print()
        table_data = TableData(cells, text_height)
        head_cell = getHeadCell(image)
        table_data.head_cell_texts = getHeadText(head_cell.getCellImage())
        table_datas.append(table_data)
    return table_datas


# 获取表格信息（单个）
def getTableData(image):
    cells = getCells(image)
    for cell in cells:
        imgs = focusImage(cell.getCellImage())
        cell_texts = getCellText(imgs)
        for text in cell_texts:
            cell.value = cell.value + text
    text_height = focusImage(cells[0].getCellImage())[0].shape[0]
    print()
    table_data = TableData(cells, text_height)
    head_cell = getHeadCell(image)
    table_data.head_cell_texts = getHeadText(head_cell.getCellImage())
    return table_data

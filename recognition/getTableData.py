from division.getCells import getCells, getHeadCell
from division.tableData import TableData
from loader.loadImages import loadImages
from texter.getBox import focusImage
from texter.getText import getHeadText, getCellText


def getTable():
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
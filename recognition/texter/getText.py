# （李奇伟 2021.07.14）

# 获取表头内容（待处理）
from ocr.ocr import recognizer
from texter.getBox import focusImage


# 获取表头内容
def getHeadText(image):
    imgs = focusImage(image)
    texts = []
    for img in imgs:
        text = recognizer.recognize(img)
        texts.append(text)
    return texts


# 获取表格单元内容（待处理）
def getCellText(images):
    texts = []
    for image in images:
        text = recognizer.recognize(image)
        texts.append(text)
    # texts.append("内容")
    # texts.append("(暂未识别)")
    return texts

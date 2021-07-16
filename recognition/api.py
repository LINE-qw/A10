#（李奇伟 2021.07.16）
from flask import Flask, request, send_from_directory, abort
from flask import render_template
from getExcel import getXls
from getTableData import *
from loader.load import *

app = Flask(__name__)

@app.route('/getExcel', methods=['GET', 'POST'])
def getExcel():
    if request.method == 'POST':
        image = request.files.get('image')
        image_name = image.filename
        emptyImages()
        image.save(getImagePath(image_name))
        img = loadImage(image_name)
        table = getTableData(img)
        name = getXls(table)
        return send_from_directory(getExcelDectionaryPath(),name, as_attachment=True)
    return 'request is not post'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
import pdfkit
import csv
import pdfkit
import os
from pypinyin import pinyin, lazy_pinyin, Style

app = Flask(__name__)
tmp = 'tmp.html'
@app.route('/')
def hello_world():
    # with open('word.csv', newline='') as File:  
    # reader = csv.reader(File)
    # for row in reader:
    #     print(row)
    nameDic = {}
    with open('csv/word.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:   
            nameDic.update({row[0]:row[1]})

    for file in os.listdir("static"):
        name = file.split('.')[0]
        pinyi = nameDic[name]
        newPage = render_template('page.html', name=name, file="/Users/ekman/Documents/pinyi/pinyi/static/" + file, pinyi=pinyi)
        with open(tmp, 'w') as fout:
            fout.write(newPage)
        pdfkit.from_file(tmp, 'pdf/'+ name +'.pdf')
    os.remove(tmp)
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
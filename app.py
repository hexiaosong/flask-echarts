# coding:utf-8
from flask import Flask,render_template,jsonify

#生成Flask实例
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    result = {'data': [ {'value': 120012, 'name': 'name2url'}, {'value': 100245, 'name': '关联关系'},]
             }
    return jsonify(result)

@app.route('/number')
def number():
    result = {'cookie_num': 1250}
    return jsonify(result)


@app.route('/check')
def check():
    return "hello world"


if __name__ == "__main__":
    #运行项目
    app.run(app.run(debug=False, port=5000, host='localhost'))

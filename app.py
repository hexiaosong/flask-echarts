# coding:utf-8

from __future__ import unicode_literals

from flask import Flask,render_template,jsonify, redirect

#生成Flask实例
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    result = {'data': [ {'value': 12, 'name': '行业一'}, {'value': 13, 'name': '行业二'},
                        {'value': 70, 'name': '行业三'}, {'value': 52, 'name': '行业四'},
                        {'value': 35, 'name': '行业五'}]
             }
    return jsonify(result)


if __name__ == "__main__":
    #运行项目
    app.run(app.run(debug=True, port=5000, host='localhost'))

# coding:utf-8
import time
import redis
from flask import Flask,render_template,jsonify
from utils.common import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/echarts1')
def yesterday_crawl_statistic():
    """昨日抓取数据统计"""
    statistic = [{'name': 'name2url', 'value': get_prod_name2url_number()},
                 {'name': '关联接口', 'value': get_hk_relationsip_api_number()}]

    return jsonify({'data': statistic})


@app.route('/echarts3')
def today_crawl_statistic():
    """昨日抓取数据统计"""
    result = {'data': [900, 312, 321,754, 500, 830, 710, 521, 504, 660, 530, 410,710, 312, 321,754, 500, 830, 0, 0, 0, 0, 0, 0]}
    return jsonify(result)


@app.route('/redis')
def number():
    """redis队列统计"""
    conn = redis.Redis(host="123.234.5.241", port=12306, password="Cqjrdsjzx&2020", db=5)
    result = {
        'cookie_number': conn.llen("cookie"),
        'cookie_expire': conn.llen("index_verify"),
        'name_to_url': conn.llen("name_to_url"),
        'relationship': conn.llen("qcc_findRelationsDetail")
    }
    time.sleep(1)
    return jsonify(result)



if __name__ == "__main__":
    app.run(app.run(debug=False, port=5000, host='localhost'))

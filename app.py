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

    return jsonify({'statistic': statistic})


@app.route('/echarts3')
def today_crawl_statistic():
    """今日抓取数据统计"""
    result = get_line_statics()
    return jsonify({'data':result})


@app.route('/number')
def number():
    """redis队列统计"""
    total_num = get_relationship_total_num()
    conn = redis.Redis(host="123.234.5.241", port=12306, password="Cqjrdsjzx&2020", db=5)
    result = {
        'cookie_number': conn.llen("cookie"),
        'cookie_expire': conn.llen("index_verify"),
        'name_to_url': conn.llen("name_to_url"),
        'relationship': conn.llen("qcc_findRelationsDetail"),
        'num1': str(total_num)[0],
        'num2': str(total_num)[1],
        'num3': str(total_num)[2],
        'num4': str(total_num)[3],
        'num5': str(total_num)[4],
        'num6': str(total_num)[5],
        'num7': str(total_num)[6],
        'num8': str(total_num)[7],
    }
    return jsonify(result)



if __name__ == "__main__":
    app.run(app.run(debug=False, port=5000, host='0.0.0.0'))

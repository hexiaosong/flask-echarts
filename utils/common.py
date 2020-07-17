# coding: utf-8
"""
Create on 2020-7-14 15:18

@author:hexiaosong
"""
import json
import datetime
from pymongo import MongoClient
from utils import project_root


def getYesterday():
    """昨日日期"""
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday.strftime('%Y-%m-%d')


def get_prod_name2url_number():
    """获取昨日name_to_url企业数量"""
    client = MongoClient("123.234.5.241", 27088)
    db = client.dbadmin
    db.authenticate('cqgcxyqcc', '$6xeOHR6Jget@DuLx')
    prod = client.prod
    colletcion = "name_to_url%s" % getYesterday()
    number = prod[colletcion].count()
    return number


def get_hk_relationsip_api_number():
    """获取关联关系抓取数量"""
    client = MongoClient("45.156.169.147", 27017)
    db = client.admin
    db.authenticate('hk', '$6xeOHR6Jget@DuLx')
    hk_prod = client.hk_prod
    colletcion = "qcc_findRelationsDetail%s" % getYesterday()
    hk_number = hk_prod[colletcion].count()
    return hk_number


def read_history_data():
    data = open(project_root + '/data/relationship_api_data.json', 'r').readlines()
    data = [json.loads(item.strip()) for item in data]
    return data


def get_relationship_total_num():
    """抓取数量总计"""
    history_data = read_history_data()
    total_num = sum([list(item.values())[0] for item in history_data])

    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    if current_date in [list(item.keys())[0] for item in history_data]:

        current_num = get_hk_relationsip_api_number()
        before_num = sum([list(item.values())[0] for item in history_data[:-1]])
        history_data[-1][current_date] = current_num
        with open(project_root+'/data/relationship_api_data.json', 'w') as f:
            for item in history_data:
                f.write(json.dumps(item) + '\n')
        total_num = current_num + before_num
    else:
        current_num = get_hk_relationsip_api_number()
        before_num = sum([list(item.values())[0] for item in history_data])
        history_data.append({current_date: current_num})
        with open(project_root + '/data/relationship_api_data.json', 'w') as f:
            for item in history_data:
                f.write(json.dumps(item) + '\n')
        total_num = current_num + before_num

    return total_num

def get_line_statics():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    client = MongoClient("123.234.5.241", 27088)
    client.dbadmin.authenticate('cqgcxyqcc', '$6xeOHR6Jget@DuLx')
    db = client.prod
    result = db['static_name_to_url'].find_one({"date": current_date})
    counts = list(result['data'].values())

    return counts




if __name__ == '__main__':
    print(get_hk_relationsip_api_number())
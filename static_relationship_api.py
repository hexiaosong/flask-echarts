# coding: utf-8
"""
Create on 2020-7-16 17:18

@author:hexiaosong
"""
import time
import pymongo
import datetime

QUERY_TIME_LIST = ["0{}:00:00".format(i) for i in range(10)] + ["{}:00:00".format(i+10) for i in range(14)]


def get_mongo_collection(collociton_name):
    client = pymongo.MongoClient("123.234.5.241", 27088)
    client.dbadmin.authenticate('cqgcxyqcc', '$6xeOHR6Jget@DuLx')
    db = client.prod
    collection = db[collociton_name]
    return collection

while True:
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    print(current_date, current_time)
    if current_time == "00:00:00":
        static_col = get_mongo_collection('static_relationship_api')
        data = {"date": current_date,
                "data": {"00": 0, "01": 0, "02": 0, "03": 0, "04": 0, "05": 0, "06": 0, "07": 0, "08": 0,
                         "09": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0,
                         "17": 0, "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0}}
        static_col.insert_one(data)

    current_hour = datetime.datetime.now().strftime('%H')
    if current_time in QUERY_TIME_LIST:
        qcc_findRelationsDetail = get_mongo_collection('qcc_findRelationsDetail')
        count = qcc_findRelationsDetail.count()

        static_col = get_mongo_collection('static_relationship_api')
        result = static_col.find_one({"date":current_date})
        result['data'][current_hour] = count
        static_col.update_one({"date":current_date}, {"$set":result})
    else:
        time.sleep(1)





# coding: utf-8
"""
Create on 2020-7-15 18:17

@author:hexiaosong
"""
import pymongo

client = pymongo.MongoClient('mongodb://192.168.34.124:27017/')

myCol = client['prod']
def col_names():
    result = myCol.list_collection_names(session=None)
    return result


coll_names = []
for i in col_names():
    if 'qcc_findRelationsDetail2020-06' in i:
        coll_names.append(i)

print(coll_names)
print(len(coll_names))
a = 0
for col in coll_names:
    a = a+1
    print(a,col)
    data = myCol[col].find({},{"_id":0,"value.Result.Name":1},no_cursor_timeout=False)
    for d in data:
        try:
            myCol['qcc_findRelationsDetail_totalname'].insert_one({'name':d['value']['Result']['Name']})
        except Exception as e:
            pass
# coding: utf-8
"""
Create on 2020-7-14 15:18

@author:hexiaosong
"""
import datetime
from pymongo import MongoClient


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
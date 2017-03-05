#coding:utf-8
'''
Created on 2017年3月5日

@author: water

'''
import os
import MySQLdb
from base.BaseConfig import DbConfig
import string
# def dbutils():
#     conn = MySQLdb.connect(host, user, passwd, port)


def db_do_select():
    pass

def db_do_insert():
    pass

names = string.letters
data = []
for index, item in enumerate(names):
    temp_value = index, item
    data.append(temp_value)


data1 = []

for item in names:
    temp_value = names.index(item), item
    data1.append(temp_value)

dbconfig = DbConfig()
conn = MySQLdb.connect(host=dbconfig.HOST, user=dbconfig.PASSWD, passwd=dbconfig.PASSWD, db=dbconfig.DB, \
                       charset='utf8')
cursor = conn.cursor()

# data = [(6, 'admin01'),(7, 'admin02'), (8, 'admin03')]

stmt = "insert into person values(%s, %s, null)"
r = cursor.executemany(stmt, data1)

print r
conn.commit()
conn.close()





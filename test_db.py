import os
import pymongo
import urllib

DB_USER = 'ako'
DB_PASSWORD = 'secret123'
myclient = pymongo.MongoClient('mongodb://' + DB_USER + ':' + DB_PASSWORD + '@ds060749.mlab.com:60749/sramako_qtest?retryWrites=false')

mydb = myclient["sramako_qtest"]
mycol = mydb["Groups"]

mydict = { "GROUP": "TEST GRP", "EMAIL": "name@gmail.com" }

x = mycol.insert_one(mydict)
print(x)
import os
import pymongo
import urllib

DB_USER = 'ako'
DB_PASSWORD = 'secret123'
db_client = pymongo.MongoClient('mongodb://' + DB_USER + ':' + DB_PASSWORD + '@ds060749.mlab.com:60749/sramako_qtest?retryWrites=false')
db = db_client["sramako_qtest"]

db_col = db["Groups"]
data = {
    "GROUP": "Second Test",
    "EMAIL": "abc@gmail.com"
}
db_col.insert_one(data)
import os
import pymongo

def get_response(msg):
    msg = msg.split()
    COMMAND = msg[0]
    COMMAND = COMMAND.lower()

    if COMMAND == 'register':
        # DB_USER = os.environ.get('DB_USER')
        # DB_PASSWORD = os.environ.get('DB_PASSWORD')

        try:
            DB_USER = 'ako'
            DB_PASSWORD = 'secret123'
            db_client = pymongo.MongoClient('mongodb://' + DB_USER + ':' + DB_PASSWORD + '@ds060749.mlab.com:60749/sramako_qtest?retryWrites=false')
            db = db_client["sramako_qtest"]
        except:
            return "DB Access FAILED."

        GROUP = ' '.join(msg[1:-1])
        GROUP = GROUP.upper()
        EMAIL = msg[-1]
        EMAIL = EMAIL.lower()

        try:
            db_col = db["Groups"]
            data = {
                "GROUP": GROUP,
                "EMAIL": EMAIL
            }
            db_col.insert_one(data)

            return 'REGISTERED >> GROUP:'+GROUP+', EMAIL:'+EMAIL

        except:
            return 'Register Operation has FAILED.'

    return "This message was not handled."
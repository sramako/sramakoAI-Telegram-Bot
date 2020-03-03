def get_response(msg):
    msg = msg.split()
    COMMAND = msg[0]
    COMMAND = COMMAND.lower()
    if COMMAND == 'register':
        GROUP = ' '.join(msg[1:-1])
        GROUP = GROUP.upper()
        EMAIL = msg[-1]
        EMAIL = EMAIL.lower()

        try:
            collection = db["Groups"]
            data = {
                "GROUP": GROUP,
                "EMAIL": EMAIL
            }
            collection.insert_one(data)

            return 'REGISTERED >> GROUP:'+GROUP+'|EMAIL:'+EMAIL

        except:
            return 'Register Operation has FAILED.'

    return "This message was not handled."
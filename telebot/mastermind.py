def get_response(msg):
    msg = msg.split()
    COMMAND = msg[0]
    COMMAND = COMMAND.lower()
    if COMMAND == 'register'
        GROUP = ' '.join(msg[1:-1])
        GROUP = GROUP.upper()
        EMAIL = msg[-1]
        EMAIL = EMAIL.lower()
        return 'GROUP:'+GROUP+'|EMAIL:'+EMAIL
    return "This message was not handled."
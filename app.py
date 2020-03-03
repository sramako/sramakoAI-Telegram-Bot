from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL
from telebot.mastermind import get_response
import os
import pymongo
import urllib

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

# DB_USER = os.environ.get('DB_USER')
# DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_USER = 'ako'
DB_PASSWORD = 'secret123'
db_client = pymongo.MongoClient('mongodb://' + DB_USER + ':' + DB_PASSWORD + '@ds060749.mlab.com:60749/sramako_qtest')
db = db_client["sramako_qtest"]

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    print("got text message :", text)

    response = get_response(text)
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    return 'ok'

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "Webhook Setup : SUCCESS"
    else:
        return "Sebhook Setup : FAILED"

@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    app.run(threaded=True)
import json
import time
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)
ListOfMessages = []

@app.route('/')
def hello_world():  # put application's code here
    return 'Messenger Flask server is running! ' \
           '<br> <a href="/status">Check status</a>'

@app.route('/status')
def status():
    return {
        'messages_count': len(ListOfMessages)
    }

@app.route("/api/mes", methods=['POST'])
def SendMessage():
    msg = request.json
    msg['timeStamp']= datetime.now()
    print(msg)
    # messages.append({ "userName":"Kolya","messageText":"Vot bi na dachu...","timeStamp":"2021-03-05T18:23:10.932973Z"})
    ListOfMessages.append(msg)
    #print(msg)
    msgtext = f"{msg['userName']} <{msg['timeStamp']}>: {msg['messageText']}"
    print(f"Всего сообщений: {len(ListOfMessages)} Посланное сообщение: {msgtext}")
    return f"Сообщение отослано успешно. Всего сообщений: {len(ListOfMessages)} ", 200

@app.route("/api/mes/<int:id>")
def GetMessage(id):
    print(id)
    if id >= 0 and id < len(ListOfMessages):
        print(ListOfMessages[id])
        return ListOfMessages[id], 200
    else:
        return "not found", 400

if __name__ == '__main__':
    app.run()

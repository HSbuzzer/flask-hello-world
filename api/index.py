import flask
from flask_cors import CORS
from requests import get
from dotenv import load_dotenv
import os
import json

load_dotenv()
app = flask.Flask(__name__)
CORS(app)

counter = 0


@app.route("/")
def home():
    global counter
    resp = flask.Response(f"Hello world! {counter} times")
    counter += 1
    resp.headers["Content-Type"] = "text/plain"
    resp.headers["Connection"] = "Keep-Alive"
    resp.headers["Keep-Alive"] = "timeout=5, max=1000"
    return resp


@app.route("/led")
def LED():
    # load last updateID
    with open('api/lastUpdate.json', 'r') as f:
        last_update = json.load(f)
    updateID = last_update['update_id'] + 1
    
    
    botUpdates = get(f'https://api.telegram.org/bot{os.getenv("BOT_TOKEN")}/getUpdates?allowed_updates=message&timeout=0&limit=1&offset={updateID}')
    update = botUpdates.json()['result']
    
    if update:
        # write to lastUpdate.json to "update_id" field
        writable = {
            "update_id": update[-1]["update_id"],
            "color": update[-1]["message"]["text"].replace("/color ", "")
        }
        with open('api/lastUpdate.json', 'w') as f:
            json.dump(writable, f)
            
        return writable["color"]
    
    else:
        return "no updates found"
    

@app.route("/test")
def test():
    command = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage?chat_id={os.getenv('CHAT_ID')}&text=operational"
    get(command)
    return f"message sent to chat {os.getenv('CHAT_ID')}"

# app.run(host="0.0.0.0")

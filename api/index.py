import flask
from flask_cors import CORS
from requests import get
from dotenv import load_dotenv
import os
from time import sleep

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


@app.route("/LED")
def LED():
    botUpdates = get(f'https://api.telegram.org/bot{os.getenv("BOT_TOKEN")}/getUpdates')
    botUpdates = botUpdates.json()
    return str(botUpdates)

@app.route("/test")
def test():
    get(f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage?chat_id={os.getenv('CHAT_ID')}&text=operational")
    return "message sent"

# app.run(host="0.0.0.0")

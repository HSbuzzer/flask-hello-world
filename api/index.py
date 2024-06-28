import flask
from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app)


@app.route("/")
def home():
    resp = flask.Response("Hello world!")
    resp.headers["Content-Type"] = "text/plain"
    resp.headers["Connection"] = "Keep-Alive"
    resp.headers["Keep-Alive"] = "timeout=5, max=1000"
    return resp


@app.route("/about")
def about():
    return "About"

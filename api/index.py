import flask
from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app)


@app.route("/")
def home():
    resp = flask.Response("Foo bar baz")
    resp.headers["Content-Type"] = "text/plain"
    return resp


@app.route("/about")
def about():
    return "About"

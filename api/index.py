from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return Response("Hello, world!", mimetype='text/plain')

@app.route('/about')
def about():
    return 'About'
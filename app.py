from distutils.log import debug
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "<p>Hello, Wodddrld!</p>"
    else:
        return "<p>Hello, Woaaarld!</p>"

@app.get('/login')
def login_get():
    return "<p>Hello, Wodddrld!</p>"

@app.post('/login')
def login_post():
    return "<p>Hello, Woaaarld!</p>"


# Dict response
@app.route("/me")
def me_api():
    return {
        "username": "Anthony",
        "pass": "okok"
    }


import json

@app.route("/tickers")
@cross_origin(origin='*')
def get_tickers():
    with open('tickers.json') as json_file:
        data = json.load(json_file)
        return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
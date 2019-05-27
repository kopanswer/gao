# -*- coding:utf8 -*-

from flask import Flask
from flask import request
from flask import jsonify, make_response
import time
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/add/<a>/<b>", methods=["GET"])
def add(a, b):
    return str(int(a) + int(b))

@app.route('/login', methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]
    if not username or not password:
        return parse_response("failed")
    if str(username) == "123" and str(password) == "123":
        return parse_response("success")
    return parse_response("wrong password or username")

@app.route('/logout', methods=["POST"])
def logout():
    logout_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    username = request.json["username"]
    return parse_response("bye, %s, logout time is %s" % (str(username), str(logout_time)))

def parse_response(result):
    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999)
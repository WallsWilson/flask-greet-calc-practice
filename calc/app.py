# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add(a, b):
    a = request.args.get('a')
    b = request.args.get('b')
    answer = a + b
    return f"<h1>{a} + {b} = {answer}"

@app.route('/sub')
def subtract(a, b):
    a = request.args.get('a')
    b = request.args.get('b')
    answer = a - b
    return f"<h1>{a} - {b} = {answer}"

@app.route('/multipy')
def multiply(a, b):
    a = request.args.get('a')
    b = request.args.get('b')
    answer = a * b
    return f"<h1>{a} * {b} = {answer}"

@app.route('/divide')
def divide(a, b):
    a = request.args.get('a')
    b = request.args.get('b')
    answer = a / b
    return f"<h1>{a} / {b} = {answer}"
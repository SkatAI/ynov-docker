# app.py
from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello, World!"

@app.route('/')
def hello():
    # Get the 'text' query parameter from the URL, default to "Hello World" if not provided
    message = request.args.get('text', 'Hello World')
    return message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


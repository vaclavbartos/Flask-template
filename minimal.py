# Example of minimal working WSGI script
from flask import Flask, make_response

application = app = Flask(__name__)

@app.route('/')
def main():
    return make_response('It works!')


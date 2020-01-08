# Example of a simple WSGI script
import flask
from flask import Flask, render_template, make_response

application = app = Flask(__name__)

# Example of redering a simple HTML page

@app.route('/')
def main():
    # Do some work...
    variable = -123
    # Render Jinja2 template, pass variables to use in the template
    # hint: to pass many variables, use **locals()
    return render_template('main.html', variable=variable)


# Example of a simple API endpoint with parameters as part of path

@app.route('/api/get/<int:id>')
def api_get(id=None):
    # hint: GET/POST pameters are stored as dict in request.args
    if id is not None and 0 <= id <= 1000:
        resp = {
            'status': 'OK',
            'data': 'abcdef1234567890'
        }
        # use "jsonify" helper function to return JSON reply
        return jsonify(resp)
    else:
        resp = {
            'err_n' : 404,
            'error' : "Document ID '{}' not found".format(id)
        }
        # second argument of "jsonify" sets HTTP response code
        return jsonify(resp, 404)

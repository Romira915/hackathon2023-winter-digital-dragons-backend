from flask import Blueprint, Flask
from flask_cors import CORS

import settings
from app.api.releases import bp_releases

app = Flask(__name__)
CORS(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin',
                         settings.FRONTEND_ORIGIN)
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.register_blueprint(bp_releases)

app.run(debug=True, host="0.0.0.0", port=80)

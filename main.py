from flask import Blueprint, Flask
from flask_cors import CORS

import settings
from app.api.releases import bp_releases

app = Flask(__name__)
CORS(app, resources={r'/*': {
    'origins': settings.FRONTEND_ORIGIN
}})


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.register_blueprint(bp_releases)

app.run(debug=True, host="0.0.0.0", port=80)

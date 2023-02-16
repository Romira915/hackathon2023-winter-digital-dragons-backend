from flask import Blueprint, jsonify, request

from app.data_access_object import t_release

bp_releases = Blueprint('bp_releases', __name__, url_prefix='/api')

DEFAULT_LIMIT = 100


@bp_releases.route('/releases')
def t_releases():
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))

    press_release = t_release.get_releases(limit)

    return jsonify(press_release)
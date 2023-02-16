
from flask import Blueprint, jsonify, request

from app.data_access_object import t_release
from app.data_access_object.db import connection

bp_releases = Blueprint('bp_releases', __name__, url_prefix='/api')

DEFAULT_LIMIT = 100


@bp_releases.route('/releases')
def t_releases():
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))

    press_release = t_release.get_releases(limit)

    return jsonify(press_release)


@bp_releases.route('/search')
def search():
    category_id = None
    prefectures_id = None
    pr_type = None
    search_word = None

    if request.args.get('category_id') is not None:
        category_id = int(request.args.get('category_id'))

    if request.args.get('prefectures_id') is not None:
        prefectures_id = int(request.args.get('prefectures_id'))

    if request.args.get('pr_type') is not None:
        pr_type = request.args.get('pr_type')

    if request.args.get('search_word') is not None:
        search_word = request.args.get('search_word')

    return "null"

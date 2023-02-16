import json

from flask import Blueprint, Response, jsonify, request

from app.data_access_object import t_release
from app.db.db import Release_DB

bp_releases = Blueprint('bp_releases', __name__, url_prefix='/api')

DEFAULT_LIMIT = 100


def fix_encoding(releases):
    return Response(json.dumps(releases, ensure_ascii=False), content_type='application/json; charset=utf-8')


@bp_releases.route('/releases')
def t_releases():
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))

    press_release = fix_encoding(t_release.get_releases(limit))

    return press_release


@bp_releases.route('/all_releases')
def all_releases():
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))

    release_db = Release_DB.get_instance()
    all_releases = fix_encoding(release_db.get_all(limit))

    return all_releases


@bp_releases.route('/search')
def search():
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))
    args = []
    if request.args.get('main_category_id') is not None:
        main_category_id = int(request.args.get('main_category_id'))
        args.append(main_category_id)
    if request.args.get('sub_category_id') is not None:
        sub_category_id = int(request.args.get('sub_category_id'))
        args.append(sub_category_id)
    if request.args.get('pr_type') is not None:
        pr_type = request.args.get('pr_type')
        args.append(pr_type)

    release_db = Release_DB.get_instance()
    results = fix_encoding(release_db.search(limit, *args))

    return results

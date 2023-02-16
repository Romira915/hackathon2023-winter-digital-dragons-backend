from flask import Blueprint, jsonify, request

from app.data_access_object import t_release

from app.db.db import Release_DB

bp_releases = Blueprint('bp_releases', __name__, url_prefix='/api')

DEFAULT_LIMIT = 100


@bp_releases.route('/releases')
def t_releases():
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))

    press_release = t_release.get_releases(limit)

    return jsonify(press_release)

@bp_releases.route('/all_releases')
def all_releases():
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))
    
    release_db = Release_DB.get_instance()
    all_releases = release_db.get_all(limit)
    
    return jsonify(all_releases)

@bp_releases.route('/search')
def search():
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))
    if request.args.get('main_category_id') is not None:
        main_category_id = int(request.args.get('main_category_id'))
    if request.args.get('sub_category_id') is not None:
        sub_category_id = int(request.args.get('sub_category_id'))
    if request.args.get('pr_type') is not None:
        pr_type = request.args.get('pr_type')
        
    release_db = Release_DB.get_instance()
    results = release_db.search(limit, main_category_id, sub_category_id, pr_type)
    
    return jsonify(results)
from flask import Blueprint, jsonify, request, Response
import json

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

    release_db = Release_DB.get_instance()
    all_releases = fix_encoding(release_db.get_all(limit))

    return all_releases


@bp_releases.route('/search')
def search():
    """"
        ・limit: 取得する記事の数。デフォルトは100。
        ・category_id: 検索するカテゴリーのID。カテゴリーIDは以下の通りです。
        ・pr_type: 検索するPRの種類。PRの種類は以下の通りです。
        ・start_date: 検索する期間の開始日。YYYY-MM-DD形式で指定します。
        ・end_date: 検索する期間の終了日。YYYY-MM-DD形式で指定します。
    """
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))
    kargs = {}
    if request.args.get('category_id') is not None:
        main_category_id = int(request.args.get('category_id'))
        kargs['main_category_id'] = main_category_id
    if request.args.get('pr_type') is not None:
        pr_type = request.args.get('pr_type')
        kargs['pr_type'] = pr_type
    if request.args.get('start_date') is not None:
        start_date = request.args.get('start_date')
        kargs['start_date'] = start_date
    if request.args.get('end_date') is not None:
        end_date = request.args.get('end_date')
        kargs['end_date'] = end_date
        
    release_db = Release_DB.get_instance()
    results = fix_encoding(release_db.search(limit, **kargs))
    
    return results
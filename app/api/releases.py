from flask import Blueprint, jsonify, request, Response
import json

from app.db.db import Release_DB

bp_releases = Blueprint('bp_releases', __name__, url_prefix='/api')

DEFAULT_LIMIT = 100


def fix_encoding(releases):
    return Response(json.dumps(releases, ensure_ascii=False), content_type='application/json; charset=utf-8')


@bp_releases.route('/releases')
def n_releases():
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))

    release_db = Release_DB.get_instance()
    all_releases = fix_encoding(release_db.get_n_releases(limit))

    return all_releases


@bp_releases.route('/search')
def search():
    """"
        ・limit: 取得する記事の数。デフォルトは100。
        ・category_id: 検索するカテゴリーのID。
        ・pr_type: 検索するPRの種類。
        ・prefecture: 検索する都道府県。
        ・industry: 検索する業種。
        ・ipo_type: 検索するIPOの種類。
        ・start_date: 検索する期間の開始日。YYYY-MM-DD形式で指定します。
        ・end_date: 検索する期間の終了日。YYYY-MM-DD形式で指定します。
    """
    limit = DEFAULT_LIMIT
    if request.args.get('limit') is not None:
        limit = int(request.args.get('limit'))
        
    kargs = {}
    search_items = ['category_id', 'pr_type', 'prefecture', 'industry', 'ipo_type', 'start_date', 'end_date']
    for item in search_items:
        if request.args.get(item) is not None:
            kargs[item] = request.args.get(item)
        
    release_db = Release_DB.get_instance()
    results = fix_encoding(release_db.search(limit, **kargs))
    
    return results
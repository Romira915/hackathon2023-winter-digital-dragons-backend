from flask import Blueprint, request, Response
import json

from app.db.db import Release_DB

bp_releases = Blueprint('bp_releases', __name__, url_prefix='/api')
DEFAULT_LIMIT = 100
SEARCH_ITEMS = ['category_id', 'pr_type', 'prefecture', 'industry', 'ipo_type', 'start_date', 'end_date']


def fix_encoding(releases):
    return Response(json.dumps(releases, ensure_ascii=False), content_type='application/json; charset=utf-8')


@bp_releases.route('/releases')
def n_releases():
    limit = int(request.args.get('limit', DEFAULT_LIMIT))
    release_db = Release_DB.get_instance()
    all_releases = fix_encoding(release_db.get_n_releases(limit))
    return all_releases


@bp_releases.route('/search')
def search():
    """"検索条件
        ・limit: 取得する記事の数。デフォルトは100。
        ・category_id: 検索するカテゴリーのID。
        ・pr_type: 検索するPRの種類。
        ・prefecture: 検索する都道府県。
        ・industry: 検索する業種。
        ・ipo_type: 検索するIPOの種類。
        ・start_date: 検索する期間の開始日。YYYY-MM-DD形式で指定します。
        ・end_date: 検索する期間の終了日。YYYY-MM-DD形式で指定します。
    """
    limit = int(request.args.get('limit', DEFAULT_LIMIT))
    search_params = {item: request.args.get(item) for item in SEARCH_ITEMS if request.args.get(item)}
    release_db = Release_DB.get_instance()
    results = fix_encoding(release_db.search(limit, **search_params))
    
    return results
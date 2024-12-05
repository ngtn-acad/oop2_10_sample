from flask import Blueprint, render_template, request, redirect, url_for
from models import Search

# Blueprintの作成
search_bp = Blueprint('search', __name__, url_prefix='/searches')


@search_bp.route('/')
def list():
    
    # データ取得
    searches = Search.select()

    return render_template('user_search.html', title='検索一覧', items=searches)

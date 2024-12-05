from flask import Blueprint, render_template, request, redirect, url_for
from models import Song

# Blueprintの作成
song_bp = Blueprint('song', __name__, url_prefix='/songs')


@song_bp.route('/')
def list():
    songs = Song.select()
    return render_template('song_list.html', title='曲一覧', items=songs)


@song_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        song = request.form['song']
        artist = request.form['artist']
        Song.create(song=song, artist=artist)
        return redirect(url_for('song.list'))
    
    return render_template('song_add.html')


@song_bp.route('/edit/<int:song_id>', methods=['GET', 'POST'])
def edit(song_id):
    song = Song.get_or_none(Song.id == song_id)
    if not song:
        return redirect(url_for('song.list'))

    if request.method == 'POST':
        song.song = request.form['song']
        song.artist = request.form['artist']
        song.save()
        return redirect(url_for('song.list'))

    return render_template('song_edit.html', song=song)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data
playlists = [
    {
        'id': 1,
        'name': 'Rock Hits',
        'genre': 'Rock',
        'songs': [
            {'title': 'Bohemian Rhapsody', 'album_art': 'rock.jpg'}
        ]
    },
    {
        'id': 2,
        'name': 'Smooth Jazz',
        'genre': 'Jazz',
        'songs': []
    }
]

@app.route('/')
def home():
    return redirect(url_for('list_playlists'))

@app.route('/playlists')
def list_playlists():
    genre = request.args.get('genre')
    if genre:
        filtered = [pl for pl in playlists if pl['genre'] == genre]
    else:
        filtered = playlists
    return render_template('list.html', playlists=filtered)

@app.route('/playlist/<int:playlist_id>')
def playlist_detail(playlist_id):
    playlist = next((p for p in playlists if p['id'] == playlist_id), None)
    return render_template('detail.html', playlist=playlist)

@app.route('/playlist/<int:playlist_id>/add', methods=['GET', 'POST'])
def add_song(playlist_id):
    playlist = next((p for p in playlists if p['id'] == playlist_id), None)
    if request.method == 'POST':
        title = request.form['title']
        album_art = request.form['album_art']
        playlist['songs'].append({'title': title, 'album_art': album_art})
        return redirect(url_for('playlist_detail', playlist_id=playlist_id))
    return render_template('add_song.html', playlist=playlist)


if __name__ == '__main__':
    app.run(debug=True)
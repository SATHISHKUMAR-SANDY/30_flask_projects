from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

movies = [
    {'id': 1, 'title': 'Inception', 'genre': 'Sci-Fi', 'poster': 'inception.jpg', 'recommendations': []},
    {'id': 2, 'title': 'The Notebook', 'genre': 'Romance', 'poster': 'notebook.jpg', 'recommendations': []},
    {'id': 3, 'title': 'Avengers: Endgame', 'genre': 'Action', 'poster': 'endgame.jpg', 'recommendations': []},
    {'id': 4, 'title': 'Interstellar', 'genre': 'Sci-Fi', 'poster': 'interstellar.jpg', 'recommendations': []}
]

@app.route('/')
def home():
    genre_filter = request.args.get('genre')
    if genre_filter:
        filtered = [m for m in movies if m['genre'] == genre_filter]
    else:
        filtered = movies
    return render_template('index.html', movies=filtered, genre_filter=genre_filter)

@app.route('/movie/<int:movie_id>', methods=['GET', 'POST'])
def movie_detail(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if not movie:
        return "Movie not found", 404

    if request.method == 'POST':
        name = request.form['name']
        reason = request.form['reason']
        movie['recommendations'].append({'name': name, 'reason': reason})
        return redirect(url_for('movie_detail', movie_id=movie_id))

    return render_template('movie_detail.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True, port=8008)

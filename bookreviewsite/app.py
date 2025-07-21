from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {'id': 1, 'title': 'The Alchemist', 'cover': 'alchemist.jpg', 'reviews': []},
    {'id': 2, 'title': '1984', 'cover': '1984.jpg', 'reviews': []},
    {'id': 3, 'title': 'To Kill a Mockingbird', 'cover': 'mockingbird.jpg', 'reviews': []}
]

@app.route('/')
def index():
    rating_filter = request.args.get('rating')
    for book in books:
        if rating_filter:
            book['filtered_reviews'] = [r for r in book['reviews'] if str(r['rating']) == rating_filter]
        else:
            book['filtered_reviews'] = book['reviews']
    return render_template("index.html", books=books, rating_filter=rating_filter)

@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return "Book not found", 404
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        rating = int(request.form['rating'])
        book['reviews'].append({'name': name, 'comment': comment, 'rating': rating})
        return redirect(url_for('book_detail', book_id=book_id))
    return render_template("book_detail.html", book=book)

if __name__ == '__main__':
    app.run(debug=True,port=8008)

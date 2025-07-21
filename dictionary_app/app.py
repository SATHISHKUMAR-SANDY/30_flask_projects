from flask import Flask, render_template, request, redirect, url_for
from data import dictionary_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        word = request.form['word'].strip().lower()
        lang = request.form.get('lang', 'en')
        return redirect(url_for('show_word', word=word, lang=lang))
    return render_template('search.html')

@app.route('/word/<word>')
def show_word(word):
    lang = request.args.get('lang', 'en')
    meaning = dictionary_data.get(word, {}).get(lang)
    icon = 'english.png' if lang == 'en' else 'tamil.png'
    return render_template('word.html', word=word, meaning=meaning, lang=lang, icon=icon)

if __name__ == '__main__':
    app.run(debug=True,port=9001)

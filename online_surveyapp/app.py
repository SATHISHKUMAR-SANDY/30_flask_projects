from flask import Flask, render_template, request, redirect, url_for
from data import responses

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'age': int(request.form['age']),
            'feedback': request.form['feedback']
        }
        responses.append(data)
        return redirect(url_for('results'))
    return render_template('survey.html')

@app.route('/results')
def results():
    age_group = request.args.get('age')
    if age_group == 'under18':
        filtered = [r for r in responses if r['age'] < 18]
    elif age_group == '18to40':
        filtered = [r for r in responses if 18 <= r['age'] <= 40]
    elif age_group == 'above40':
        filtered = [r for r in responses if r['age'] > 40]
    else:
        filtered = responses
    return render_template('results.html', responses=filtered, selected=age_group)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from data import appointments

app = Flask(__name__)

@app.route('/')
def home():
    date_filter = request.args.get('date')
    filtered = [a for a in appointments if a['date'] == date_filter] if date_filter else appointments
    return render_template('home.html', appointments=filtered, date=date_filter)

@app.route('/appointment/<int:app_id>')
def appointment_detail(app_id):
    appointment = next((a for a in appointments if a['id'] == app_id), None)
    return render_template('detail.html', appointment=appointment)

@app.route('/add', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        new = {
            "id": len(appointments) + 1,
            "name": request.form['name'],
            "date": request.form['date'],
            "time": request.form['time'],
            "desc": request.form['desc']
        }
        appointments.append(new)
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)

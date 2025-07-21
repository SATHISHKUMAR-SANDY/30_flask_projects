from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

logs = []
log_id_counter = 1

@app.route('/')
def home():
    return redirect(url_for('logs_page'))

@app.route('/add-log', methods=['GET', 'POST'])
def add_log():
    global log_id_counter
    if request.method == 'POST':
        workout = request.form['workout']
        duration = request.form['duration']
        date = request.form['date']
        icon = request.form['icon']
        logs.append({
            'id': log_id_counter,
            'workout': workout,
            'duration': duration,
            'date': date,
            'icon': icon
        })
        log_id_counter += 1
        return redirect(url_for('logs_page'))
    return render_template("add_log.html")

@app.route('/logs')
def logs_page():
    filter_date = request.args.get('date')
    if filter_date:
        filtered_logs = [log for log in logs if log['date'] == filter_date]
    else:
        filtered_logs = logs
    return render_template("logs.html", logs=filtered_logs, filter_date=filter_date)

@app.route('/log/<int:log_id>')
def log_detail(log_id):
    log = next((log for log in logs if log['id'] == log_id), None)
    if not log:
        return "Log not found", 404
    return render_template("log_detail.html", log=log)
    
if __name__ == '__main__':
    app.run(debug=True,port=9003)

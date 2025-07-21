from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
subscribers = []

@app.route('/')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = datetime.now().strftime("%Y-%m-%d")
        subscribers.append({"name": name, "email": email, "date": date})
        return redirect(url_for('thank_you'))
    return render_template("signup.html")

@app.route('/thankyou')
def thank_you():
    return render_template("thankyou.html")

@app.route('/subscribers')
def show_subscribers():
    filter_date = request.args.get('date')
    if filter_date:
        filtered = [s for s in subscribers if s["date"] == filter_date]
    else:
        filtered = subscribers
    return render_template("subscribers.html", subs=filtered)

if __name__ == '__main__':
    app.run(debug=True)

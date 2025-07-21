from flask import Flask, render_template, request, redirect, url_for
from data import parking_slots

app = Flask(__name__)

@app.route('/')
def show_slots():
    filter_date = request.args.get("date", "2025-07-21")
    filtered = [slot for slot in parking_slots if slot["date"] == filter_date]
    return render_template("slots.html", slots=filtered, date=filter_date)

@app.route('/book/<int:slot_id>', methods=['GET', 'POST'])
def book(slot_id):
    selected = next((s for s in parking_slots if s["id"] == slot_id), None)
    if request.method == 'POST':
        selected["available"] = False
        return redirect(url_for("confirm", slot=selected["slot"]))
    return render_template("book.html", slot=selected)

@app.route('/confirm')
def confirm():
    return render_template("confirm.html", slot=request.args.get("slot"))

if __name__ == "__main__":
    app.run(debug=True)

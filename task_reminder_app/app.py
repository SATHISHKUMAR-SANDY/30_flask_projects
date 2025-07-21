from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

reminders = [
    {"id": 1, "task": "Pay bills", "due": "2025-07-22"},
    {"id": 2, "task": "Buy groceries", "due": "2025-07-23"},
]

@app.route('/')
@app.route('/reminders')
def show_reminders():
    return render_template("reminders.html", reminders=reminders)

@app.route('/add', methods=["GET", "POST"])
def add_reminder():
    if request.method == "POST":
        new_id = max([r["id"] for r in reminders]) + 1 if reminders else 1
        new_task = {
            "id": new_id,
            "task": request.form["task"],
            "due": request.form["due"]
        }
        reminders.append(new_task)
        return redirect(url_for("show_reminders"))
    return render_template("add_reminder.html")

@app.route('/delete/<int:rid>')
def delete_reminder(rid):
    global reminders
    reminders = [r for r in reminders if r["id"] != rid]
    return redirect(url_for("show_reminders"))

if __name__ == '__main__':
    app.run(debug=True)

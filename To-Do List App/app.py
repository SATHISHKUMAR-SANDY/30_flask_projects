from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Buy groceries", "description": "Milk, Bread", "status": "pending"},
    {"id": 2, "title": "Call Mom", "description": "Check in", "status": "done"},
    {"id": 3, "title": "Read book", "description": "Flask Chapter", "status": "pending"}
]

@app.route('/')
def home():
    completed = request.args.get('completed')
    if completed == 'true':
        filtered = [t for t in tasks if t['status'] == 'done']
    else:
        filtered = tasks
    return render_template("home.html", tasks=filtered)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    description = request.form.get('description')
    new_id = max([t["id"] for t in tasks]) + 1 if tasks else 1
    tasks.append({"id": new_id, "title": title, "description": description, "status": "pending"})
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True,port=8003)

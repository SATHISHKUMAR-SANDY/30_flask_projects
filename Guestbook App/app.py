from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy in-memory storage
guest_entries = []

@app.route('/')
def index():
    return render_template("index.html", entries=guest_entries)

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        entry_id = len(guest_entries)
        guest_entries.append({
            'id': entry_id,
            'name': name,
            'message': message
        })
        return redirect(url_for('index'))
    return render_template("add_entry.html")

@app.route('/entry/<int:entry_id>')
def entry_detail(entry_id):
    if 0 <= entry_id < len(guest_entries):
        entry = guest_entries[entry_id]
        return render_template("entry_detail.html", entry=entry)
    return "Entry not found!", 404

if __name__ == "__main__":
    app.run(debug=True)

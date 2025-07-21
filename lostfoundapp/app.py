from flask import Flask, render_template, request, redirect, url_for
from data import items

app = Flask(__name__)

@app.route('/')
def home():
    status_filter = request.args.get('status')
    filtered = [item for item in items if item["status"] == status_filter] if status_filter else items
    return render_template("home.html", items=filtered, status=status_filter)

@app.route('/item/<int:item_id>')
def item_detail(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    return render_template("item_detail.html", item=item)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        new_id = len(items) + 1
        new_item = {
            "id": new_id,
            "title": request.form['title'],
            "status": request.form['status'],
            "image": request.form['image'],  # Just filename, must be uploaded manually
            "description": request.form['description']
        }
        items.append(new_item)
        return redirect(url_for('home'))
    return render_template("add_item.html")

if __name__ == '__main__':
    app.run(debug=True)

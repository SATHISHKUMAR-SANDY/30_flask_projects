from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "phone": "123-456-7890",
        "city": "Chennai"
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "email": "bob@example.com",
        "phone": "987-654-3210",
        "city": "Delhi"
    }
]

@app.route('/')
def home():
    city_filter = request.args.get('city')
    if city_filter:
        filtered = [c for c in contacts if c['city'].lower() == city_filter.lower()]
    else:
        filtered = contacts
    return render_template("list.html", contacts=filtered)

@app.route('/contact/<int:cid>')
def contact_details(cid):
    contact = next((c for c in contacts if c["id"] == cid), None)
    if contact:
        return render_template("contact_details.html", contact=contact)
    return "Contact not found", 404

@app.route('/add', methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        new_id = max(c["id"] for c in contacts) + 1 if contacts else 1
        new_contact = {
            "id": new_id,
            "name": request.form["name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "city": request.form["city"]
        }
        contacts.append(new_contact)
        return redirect(url_for("home"))
    return render_template("add_contact.html")

if __name__ == '__main__':
    app.run(debug=True,port=9000)

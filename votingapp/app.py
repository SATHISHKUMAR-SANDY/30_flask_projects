from flask import Flask, render_template, request, redirect, url_for
from data import vote_data

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('vote_page'))

@app.route('/vote/', methods=['GET', 'POST'])
def vote_page():
    if request.method == 'POST':
        vote_id = int(request.form['option'])
        for opt in vote_data["options"]:
            if opt["id"] == vote_id:
                opt["votes"] += 1
                break
        return redirect(url_for('results_page', selected=vote_id))
    
    return render_template("vote.html", options=vote_data["options"])

@app.route('/results/')
def results_page():
    selected = request.args.get("selected", type=int)
    return render_template("results.html", options=vote_data["options"], selected=selected)

if __name__ == "__main__":
    app.run(debug=True)

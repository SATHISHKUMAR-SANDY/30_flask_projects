from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy poll data
poll_question = "What is your favorite programming language?"
options = ["Python", "JavaScript", "Java", "C++"]
votes = {opt: 0 for opt in options}

@app.route('/poll', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        selected = request.form.get("language")
        if selected in votes:
            votes[selected] += 1
        return redirect(url_for('result', voted=selected))
    return render_template("poll.html", question=poll_question, options=options)

@app.route('/result')
def result():
    user_vote = request.args.get("voted")
    return render_template("result.html", votes=votes, user_vote=user_vote)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            marks = float(request.form.get('marks'))
            return redirect(url_for('result', grade=marks))
        except ValueError:
            return "Invalid input! Please enter a number."
    return render_template("form.html")

@app.route('/result')
def result():
    grade = request.args.get("grade", type=float)
    return render_template("result.html", marks=grade)

if __name__ == "__main__":
    app.run(debug=True)

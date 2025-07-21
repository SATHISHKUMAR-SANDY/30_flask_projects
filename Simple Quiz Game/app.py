from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

quiz_data = [
    {
        "question": "What is the capital of India?",
        "image": "india.png",
        "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which language is used for web development?",
        "image": "",
        "options": ["Python", "HTML", "CSS", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "What does HTML stand for?",
        "image": "",
        "options": [
            "Hyper Trainer Marking Language",
            "Hyper Text Marketing Language",
            "Hyper Text Markup Language",
            "Hyper Text Markup Leveler"
        ],
        "answer": "Hyper Text Markup Language"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        user_answers = []
        for i in range(len(quiz_data)):
            answer = request.form.get(f"question{i}")
            user_answers.append(answer)
        return redirect(url_for("result", answers=",".join(user_answers)))
    return render_template("quiz.html", quiz_data=quiz_data)

@app.route("/result/")
def result():
    user_answers = request.args.get("answers").split(",")
    score = 0
    for i, answer in enumerate(user_answers):
        if answer == quiz_data[i]["answer"]:
            score += 1
    return render_template("result.html", score=score, total=len(quiz_data))

if __name__ == "__main__":
    app.run(debug=True, port=8005)

from flask import Flask,request,render_template,redirect,url_for


app = Flask(__name__)


all_feedbacks = []

@app.route("/",methods =['GET','POST'])
def form():
    if request.method == 'POST':
        feed_back = request.form.get("feedback")
        all_feedbacks.append(feed_back)
        return redirect(url_for("thank"))
    return render_template("form.html")



@app.route('/thankyou')
def thank():
    return render_template("thankyou.html")




@app.route("/showfeedback")
def show():
    return render_template("show.html",all = all_feedbacks)

if __name__ == "__main__":
    app.run(debug=True,port=8006)

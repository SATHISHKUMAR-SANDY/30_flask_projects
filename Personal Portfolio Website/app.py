from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


projects = [
    {'id': 1, 'title': 'Portfolio Website', 'description': 'My personal website using Flask.'},
    {'id': 2, 'title': 'Blog App', 'description': 'A simple blogging platform.'},
    {'id': 3, 'title': 'AI Chatbot', 'description': 'Chatbot with Python + Flask.'}
]

@app.route('/')
def home_page():

    return render_template("home.html")

@app.route('/about')
def about_page():

    return render_template("about.html")


@app.route('/contact',methods=['GET','POST'])
def contact_page():

    if request.method == 'POST':
        c_name = request.form.get("company_name")
        email = request.form.get("email")
        city = request.form.get("city")

        return redirect(url_for("success"))



    return render_template("contact.html")


@app.route('/project')
def projects_page():

    return render_template("projects.html",projects =projects)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route('/project/<int:project_id>')
def project_detail(project_id):

    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return render_template('project_detail.html', project=project)
    return "Project not found", 404


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask,render_template,request,redirect,url_for


app = Flask(__name__)

blogs = [
    {
        "id": 1,
        "title": "Getting Started with Flask",
        "author": "Sathish Kumar",
        "date": "2025-07-19",
        "tags": ["flask", "python", "webdev"],
        "summary": "Learn how to set up your first Flask web app step-by-step.",
        "content": "Flask is a lightweight web framework in Python. In this tutorial, we will build a simple app with routes, templates, and static files..."
    },
    {
        "id": 2,
        "title": "Understanding Jinja2 Templates",
        "author": "Sathish Kumar",
        "date": "2025-07-18",
        "tags": ["jinja2", "templating", "flask"],
        "summary": "A quick guide to using Jinja2 templating in Flask applications.",
        "content": "Jinja2 allows dynamic HTML rendering in Flask. With blocks, extends, and variables, you can create reusable layouts..."
    },
    {
        "id": 3,
        "title": "Styling with Bootstrap in Flask",
        "author": "Sathish Kumar",
        "date": "2025-07-17",
        "tags": ["bootstrap", "css", "flask"],
        "summary": "Add responsive and modern styling using Bootstrap in your Flask project.",
        "content": "Bootstrap is a powerful CSS framework. In this blog, we'll integrate Bootstrap via CDN and build a responsive layout..."
    },
    {
        "id": 4,
        "title": "Handling Forms in Flask",
        "author": "Sathish Kumar",
        "date": "2025-07-16",
        "tags": ["forms", "post", "request.form"],
        "summary": "Learn how to create and handle forms using Flask's request object.",
        "content": "Flask allows you to handle form data using `request.form`. In this article, we will create a contact form and store the input data..."
    }
]


@app.route("/home")

@app.route("/")
def home_page():
    return render_template("home.html",blogs = blogs)

@app.route("/post/<int:id>")

def full_post(id):
    u_id = id
    post = next( p  for p in blogs if u_id == p['id'] )
    return render_template("full_post.html",post=post)



@app.route("/admin",methods = ['GET','POST'])
def add_post():
    if request.method == 'POST':
        title = request.form.get('name')
        content = request.form.get('content')
        return redirect(url_for('success_page'))
    return render_template("admin.html")


@app.route('/success')
def success_page():
    return render_template("success.html")


@app.route('/search')
def search():
    return render_template("search.html")


@app.route('/results')
def show_results():
    query = request.args.get('q', '').lower()
    filtered = [b for b in blogs if query in b['title'].lower()]
    return render_template('results.html', blogs=filtered, query=query)

if __name__ == '__main__':
    app.run(debug=True,port=8000)
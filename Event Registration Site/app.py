from  flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

events = [
    {
        "id": 1,
        "title": "Python Bootcamp",
        "date": "2025-08-10",
        "location": "Chennai",
        "description": "A 2-day hands-on Python bootcamp for beginners.",
        "tags": ["python", "bootcamp", "beginner"]
    },
    {
        "id": 2,
        "title": "Web Development Workshop",
        "date": "2025-08-15",
        "location": "Coimbatore",
        "description": "Learn HTML, CSS, JavaScript, and Flask basics in 1 day.",
        "tags": ["web", "html", "css", "flask"]
    },
    {
        "id": 3,
        "title": "AI & ML Conference",
        "date": "2025-09-01",
        "location": "Bangalore",
        "description": "Join top speakers on AI, ML, and real-world applications.",
        "tags": ["ai", "ml", "conference"]
    },
    {
        "id": 4,
        "title": "Data Science Meetup",
        "date": "2025-08-25",
        "location": "Hyderabad",
        "description": "Network with data scientists and share ideas.",
        "tags": ["data", "meetup", "networking"]
    }
]



@app.route('/')
@app.route('/home')
def home_page():

    return render_template("home.html",events=events)


@app.route('/event')
def Events():
    e_id = request.args.get('id',"")
    e_id = int(e_id)

    event = next( e for e in events if e_id == e['id'])
    return render_template("event_details.html",event = event)

@app.route('/reg',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('event_name')

        return  redirect(url_for('thank'))
    
    return render_template('register.html')
    
@app.route('/thank')
def thank():
    return render_template("thank.html")



if __name__ == "__main__":
    app.run(debug=True,port=8001)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jobs = [
    {'id': 1, 'title': 'Software Engineer', 'department': 'IT', 'company': 'TechCorp', 'logo': 'techcorp.png', 'applications': []},
    {'id': 2, 'title': 'HR Manager', 'department': 'HR', 'company': 'PeopleFirst', 'logo': 'peoplefirst.png', 'applications': []},
    {'id': 3, 'title': 'Data Analyst', 'department': 'IT', 'company': 'DataX', 'logo': 'datax.png', 'applications': []},
    {'id': 4, 'title': 'Marketing Lead', 'department': 'Marketing', 'company': 'Brandly', 'logo': 'brandly.png', 'applications': []},
]

@app.route('/')
def index():
    dept_filter = request.args.get('dept')
    if dept_filter:
        filtered_jobs = [job for job in jobs if job['department'] == dept_filter]
    else:
        filtered_jobs = jobs
    return render_template('index.html', jobs=filtered_jobs, dept_filter=dept_filter)

@app.route('/job/<int:job_id>', methods=['GET', 'POST'])
def job_detail(job_id):
    job = next((j for j in jobs if j['id'] == job_id), None)
    if not job:
        return "Job not found", 404

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        resume = request.form['resume']
        job['applications'].append({'name': name, 'email': email, 'resume': resume})
        return redirect(url_for('success'))

    return render_template('job_detail.html', job=job)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True, port=8008)

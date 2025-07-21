from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
bucket_list = []
counter = 1

@app.route('/')
def home():
    return redirect(url_for('list_destinations'))

@app.route('/add', methods=['GET', 'POST'])
def add_destination():
    global counter
    if request.method == 'POST':
        name = request.form['name']
        region = request.form['region']
        image = request.form['image']
        desc = request.form['desc']
        bucket_list.append({
            'id': counter,
            'name': name,
            'region': region,
            'image': image,
            'desc': desc
        })
        counter += 1
        return redirect(url_for('list_destinations'))
    return render_template('add.html')

@app.route('/destinations')
def list_destinations():
    region = request.args.get('region')
    if region:
        filtered = [d for d in bucket_list if d['region'] == region]
    else:
        filtered = bucket_list
    return render_template('list.html', destinations=filtered)

@app.route('/destination/<int:dest_id>')
def destination_detail(dest_id):
    destination = next((d for d in bucket_list if d['id'] == dest_id), None)
    return render_template('detail.html', destination=destination)



if __name__ == '__main__':
    app.run() 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy pet data
pets = [
    {'id': 0, 'name': 'Tommy', 'type': 'Dog', 'age': 2, 'image': 'dog.png', 'adopted': False},
    {'id': 1, 'name': 'Whiskers', 'type': 'Cat', 'age': 1, 'image': 'dog.png', 'adopted': False}
]

@app.route('/')
def index():
    return render_template('index.html', pets=pets)

@app.route('/pet/<int:pet_id>')
def pet_detail(pet_id):
    pet = next((p for p in pets if p['id'] == pet_id), None)
    if pet:
        return render_template('pet_detail.html', pet=pet)
    return "Pet not found", 404

@app.route('/adopt/<int:pet_id>', methods=['POST'])
def adopt_pet(pet_id):
    pet = next((p for p in pets if p['id'] == pet_id), None)
    if pet:
        pet['adopted'] = True
        return redirect(url_for('adoption_success', name=pet['name'], adopted='yes'))
    return "Pet not found", 404

@app.route('/success')
def adoption_success():
    name = request.args.get('name')
    status = request.args.get('adopted')
    return render_template('adoption_success.html', name=name, status=status)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy weather data
weather_data = {
    "chennai": {"temp": "34°C", "desc": "Sunny", "icon": "sunny.png"},
    "mumbai": {"temp": "30°C", "desc": "Cloudy", "icon": "cloudy.png"},
    "delhi": {"temp": "28°C", "desc": "Rainy", "icon": "rainy.png"}
}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/check-weather', methods=['POST'])
def check_weather():
    city = request.form.get("city", "").lower()
    if city in weather_data:
        return redirect(url_for('show_weather', city=city))
    else:
        return redirect(url_for('error'))

@app.route('/weather/<city>')
def show_weather(city):
    data = weather_data.get(city.lower())
    return render_template("weather.html", city=city.title(), data=data)

@app.route('/error')
def error():
    return render_template("error.html")

if __name__ == '__main__':
    app.run(debug=True)

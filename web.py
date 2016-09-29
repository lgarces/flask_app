from flask import Flask, render_template, request
import weather
import os
app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get('address')
	forecast = None
	if address:
		forecast = weather.get_weather(address)
	return render_template('index.html', forecast=forecast)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)


#WEATHER
import forecastio
from geopy.geocoders import Nominatim

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(address):
	api_key = os.environ['FORECASTIO_API_KEY']
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	latitude = location.latitude
	longitude = location.longitude
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	summary = forecast.summary
	temperature = forecast.temperature
	return "{} and {}° at {}".format(summary, temperature, address)
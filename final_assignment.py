from flask import Flask, render_template, request
import yelp_api
import os
app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get('address')
	if address:
		businesses = yelp_api.get_businesses(location, term)
	else:
		businesses = None
	#?businesses = business_lookup
	return render_template('index.html', businesses=businesses)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)


#YELP_API
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
	auth = Oauth1Authenticator(
		consumer_key=os.environ['CONSUMER_KEY'],
		consumer_secret=os.environ['CONSUMER_SECRET'],
		token=os.environ['TOKEN'],
		token_secret=os.environ['TOKEN_SECRET']
	)

	client = Client(auth)

	params = {
		'term': term,
		'lang': 'en',
		'limit': 3
	}

	response = client.search(location, **params)

	businesses = []

	for business in response.businesses:
		#print(business.name, business.rating, business.phone)
		businesses.append({"name": business.name,
			"rating": business.rating,
			"phone": business.phone
		})

	return businesses

businesses = get_businesses('New York City', 'cocktails')

print(businesses)

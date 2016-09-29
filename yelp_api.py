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

businesses = get_businesses('New York City', 'food')

print(businesses)

#all of lession 12 from apis was lost on me because
#i can't tell when i should be using the bash terminal
#or the actual python environment. if i try to use the import
#command in python it doesn't work and if i try to do most of
#the commands (like math) in the bash one it doesn't work
#import only works in python but not bash
#pip install only works in bash not python

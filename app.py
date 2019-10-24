from flask import Flask, request
from flask_restful import Resource, Api
import requests
import json
import os

app = Flask(__name__)
api = Api(app)

class Movie(Resource):

    def get(self, id): 
        id = id.split('{')[1].strip('}')
        URL = 'https://api.themoviedb.org/3/movie/' + id
        PARAMS = {'api_key': os.environ['MOVIE_API_KEY'], 'language':'en-US'}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()  
        return data, 200

if __name__ == "__main__":
  app.run()
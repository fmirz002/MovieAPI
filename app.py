from flask import Flask, request
from flask_restful import Resource, Api
import requests
import json
import os

app = Flask(__name__)
api = Api(app)

class Search(Resource):
    def get(self): 
        if 'query' not in request.args:
            return {message: "Incorrectly formatted request"}, 400
        query = request.args['query']
        PARAMS = {'api_key':os.environ['MOVIE_API_KEY'], 'language':'en-US', 'page':'1', 'query':query}
        r = requests.get(url = 'https://api.themoviedb.org/3/search/movie', params = PARAMS)
        data = r.json()
        return data, 200

class Movie(Resource):
    def get(self, id): 
        if len(id) < 3:
            return {message: "Incorrectly formatted request"}, 400
        if id[0] != '$' or id[1] != '{' or id[-1] != '}':
            return {message: "Incorrectly formatted request"}, 400
        id = id.split('{')[1].strip('}')
        if id.isdigit() == False:
            return {message: "Incorrectly formatted request"}, 400
        URL = 'https://api.themoviedb.org/3/movie/' + id
        PARAMS = {'api_key': os.environ['MOVIE_API_KEY'], 'language':'en-US'}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()  
        return data, 200

class Show(Resource):
    def get(self, id): 
        if len(id) < 3:
            return {message: "Incorrectly formatted request"}, 400
        if id[0] != '$' or id[1] != '{' or id[-1] != '}':
            return {message: "Incorrectly formatted request"}, 400
        id = id.split('{')[1].strip('}')
        if id.isdigit() == False:
            return {message: "Incorrectly formatted request"}, 400
        URL = 'https://api.themoviedb.org/3/tv/' + id
        PARAMS = {'api_key': os.environ['MOVIE_API_KEY'], 'language':'en-US'}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()  
        return data, 200

api.add_resource(Movie, "/movie/<string:id>")
api.add_resource(Show, "/movie/<string:id>")
api.add_resource(Search, "/search")

if __name__ == "__main__":
  app.run()
import os
import sys
sys.path.append(os.path.abspath('../../../'))
from flask import Flask
from flask_restful import Resource, Api, reqparse
from cheapBuy.code.web_scrappers.web_scrapper import scrapper
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

class Scrap(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('link',required=True)

		args = parser.parse_args()

		results = scrapper(args['link'])
		print(results)
		return results, 200
	pass


api.add_resource(Scrap, '/scrap')

if __name__ == '__main__':
	app.run(debug=True, port=8080, host="0.0.0.0")  # run our Flask app

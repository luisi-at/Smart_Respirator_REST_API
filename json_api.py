# Adapted for use from: https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3, accessed 09/06/2019

import json
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Need to figure out how to store the data

data = [
    {
        "airQualityEstimate": 10,
        "latitude": 51,
        "longitude": 0
    },
    {
        "airQualityEstimate": 101,
        "latitude": 51.5,
        "longitude": 0.6
    },
    {
        "airQualityEstimate": 200,
        "latitude": 51.6,
        "longitude": -0.4
    }
]

class PollutionData(Resource):

    def get(self):
        jsonString = json.dumps(data) # Write data to string in memory

        return jsonString, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("airQualityEstimate")
        parser.add_argument("latitude")
        parser.add_argument("longitude")
        args = parser.parse_args()

        pollutionPoint = {
            "airQualityEstimate" : args["airQualityEstimate"],
            "latitude" : args["latitude"],
            "longitude": args["longitude"]
        }

        data.append(pollutionPoint)
        jsonString = json.dumps(data) # Write data to string in memory
        return jsonString, 201



api.add_resource(PollutionData, "/data")
app.run(host='192.168.206')

# Adapted for use from: https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3, accessed 09/06/2019

import json
from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource, reqparse
import datetime
import dateutil.parser as dateparse

app = Flask(__name__)
api = Api(app)

# Need to figure out how to store the data

data = [
    {
        "airQualityEstimate": 120,
        "latitude": 51.491331,
        "longitude": -0.191679,
        "dateTaken": "2019-06-09T0:0:0+0000"
    },
    {
        "airQualityEstimate": 160,
        "latitude": 51.491634,
        "longitude": -0.192083,
        "dateTaken": "2019-06-09T0:0:0+0000"
    },
    {
        "airQualityEstimate": 200,
        "latitude": 51.492451,
        "longitude": -0.190642,
        "dateTaken": "2019-06-09T0:0:0+0000"
    },
    {
        "airQualityEstimate": 200,
        "latitude": 51.492451,
        "longitude": -0.190642,
        "dateTaken": "2019-06-10T0:0:0+0000"
    }
]

class PollutionDataAll(Resource):

    def get(self):
        #jsonString = json.dumps(data, sort_keys=True) # Write data to string in memory
        return data, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('airQualityEstimate', type=int)
        parser.add_argument('latitude', type=float)
        parser.add_argument('longitude', type=float)
        parser.add_argument('dateTaken', type=string)
        args = parser.parse_args()

        pollutionPoint = {
            "airQualityEstimate" : args["airQualityEstimate"],
            "latitude" : args["latitude"],
            "longitude": args["longitude"],
            "dateTaken": args["dateTaken"]
        }

        data.append(pollutionPoint)

        return data, 201

class PollutionDataByDate(Resource):

    def get(self, date):
        returnData = [] # Empty array to return
        # Convert the incoming query into an actual datetime object
        #searchDate = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S')
        searchDate = dateparse.parse(date)
        # strip out the time to get the date
        searchDate.isoformat()
        searchDate = searchDate.date()

        # Search through the array, inspecting each date
        for entry in data:
            entryDate = dateparse.parse(entry["dateTaken"])
            # Should already return a datetime from the parser, get the date only
            # We're not concerned about the time for this proof-of-concept
            entryDate = entryDate.date()
            if(searchDate == entryDate):
                returnData.append(entry)

        # Check if the array is empty
        if not returnData:
            # resource does not exist for that query
            return 404

        # Otherwise return the array and the status code
        return returnData, 200








api.add_resource(PollutionDataAll, "/data")
api.add_resource(PollutionDataByDate, "/data/<string:date>") # Query by the date sent from the app
#app.run(host='192.168.1.206',port=5000)
app.run(debug=True)

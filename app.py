from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from geopy.distance import geodesic

app = Flask(__name__)
api = Api(app)

# In-memory database
properties_db = [
    {
        'id': 1,
        'address': '123 Main St',
        'price': 250000,
        'latitude': 37.7749,
        'longitude': -122.4194
    },
    {
        'id': 2,
        'address': '456 Elm St',
        'price': 350000,
        'latitude': 37.7751,
        'longitude': -122.4189
    },
    {
        'id': 3,
        'address': '789 Oak St',
        'price': 450000,
        'latitude': 37.7765,
        'longitude': -122.4192
    }
]

class Properties(Resource):
    def get(self):
        # Get the user's location from the query string
        user_location = request.args.get('location')
        
        # Split the location string into latitude and longitude
        user_lat, user_lon = user_location.split(',')
        
        # Convert the latitude and longitude strings to floats
        user_lat = float(user_lat)
        user_lon = float(user_lon)
        
        # Calculate the distance between the user's location and each property in the database
        properties = []
        for property in properties_db:
            property_lat = property['latitude']
            property_lon = property['longitude']
            distance = geodesic((user_lat, user_lon), (property_lat, property_lon)).miles
            if distance <= 1:  # only include properties within 1 mile of the user's location
                properties.append(property)
        
        # Return the properties that are within 1 mile of the user's location
        return jsonify(properties)

api.add_resource(Properties, '/properties')

if __name__ == '__main__':
  app.run(debug=True)
  # app.run(host='0.0.0.0', port=8080)

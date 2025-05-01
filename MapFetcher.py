# ri_map_fetcher.py

import requests

class RI_MapFetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_town_coords(self, town_name):
        geocode_url = f'https://www.mapquestapi.com/geocoding/v1/address?key={self.api_key}&location={town_name},RI'
        response = requests.get(geocode_url)
        response.raise_for_status()
        data = response.json()
        loc = data['results'][0]['locations'][0]['latLng']
        return loc['lat'], loc['lng']

    def get_traffic_incidents(self, bounding_box='42,-71,41,-72'):
        traffic_url = f'https://www.mapquestapi.com/traffic/v2/incidents?key={self.api_key}&boundingBox={bounding_box}&filters=construction,incidents'
        response = requests.get(traffic_url)
        response.raise_for_status()
        data = response.json()
        return data.get('incidents', [])

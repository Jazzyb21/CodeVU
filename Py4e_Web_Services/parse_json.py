import json

data = '''
[{
            "address_components": [{
                    "long_name": "1403",
                    "short_name": "1403",
                    "types": [
                        "street_number"
                    ]
                }, {
                    "long_name": "East Broadway",
                    "short_name": "E Broadway",
                    "types": [
                        "route"
                    ]
                }, {
                    "long_name": "Columbia",
                    "short_name": "Columbia",
                    "types": [
                        "locality",
                        "political"
                    ]
                }, {
                    "long_name": "Columbia Township",
                    "short_name": "Columbia Township",
                    "types": [
                        "administrative_area_level_3",
                        "political"
                    ]
                }, {
                    "long_name": "Boone County",
                    "short_name": "Boone County",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                }, {
                    "long_name": "Missouri",
                    "short_name": "MO",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                }, {
                    "long_name": "United States",
                    "short_name": "US",
                    "types": [
                        "country",
                        "political"
                    ]
                }, {
                    "long_name": "65201",
                    "short_name": "65201",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "1403 E Broadway, Columbia, MO 65201, USA",
            "geometry": {
                "location": {
                    "lat": 38.951585,
                    "lng": -92.31964139999999
                },
                "location_type": "ROOFTOP",
                "viewport": {
                    "northeast": {
                        "lat": 38.9529339802915,
                        "lng": -92.31829241970848
                    },
                    "southwest": {
                        "lat": 38.95023601970851,
                        "lng": -92.32099038029149
                    }
                }
            },
            "place_id": "ChIJ9SFrAOm33IcRZxy8c1d0YJE",
            "types": [
                "establishment",
                "point_of_interest",
                "university"
            ]
        }, {
            "address_components": [{
                    "long_name": "180",
                    "short_name": "180",
                    "types": [
                        "street_number"
                    ]
                }, {
                    "long_name": "Fort Washington Avenue",
                    "short_name": "Fort Washington Ave",
                    "types": [
                        "route"
                    ]
                }, {
                    "long_name": "Manhattan",
                    "short_name": "Manhattan",
                    "types": [
                        "political",
                        "sublocality",
                        "sublocality_level_1"
                    ]
                }, {
                    "long_name": "New York",
                    "short_name": "New York",
                    "types": [
                        "locality",
                        "political"
                    ]
                }, {
                    "long_name": "New York County",
                    "short_name": "New York County",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                }, {
                    "long_name": "New York",
                    "short_name": "NY",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                }, {
                    "long_name": "United States",
                    "short_name": "US",
                    "types": [
                        "country",
                        "political"
                    ]
                }, {
                    "long_name": "10032",
                    "short_name": "10032",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "180 Fort Washington Ave, New York, NY 10032, USA",
            "geometry": {
                "location": {
                    "lat": 40.8411687,
                    "lng": -73.9419685
                },
                "location_type": "ROOFTOP",
                "viewport": {
                    "northeast": {
                        "lat": 40.84251768029149,
                        "lng": -73.94061951970849
                    },
                    "southwest": {
                        "lat": 40.83981971970849,
                        "lng": -73.94331748029151
                    }
                }
            },
            "place_id": "ChIJMypJVGj3wokRcSvAsUgqYfc",
            "types": [
                "doctor",
                "establishment",
                "health",
                "point_of_interest"
            ]
        }
    ]'''

deserialized_json = json.loads(data)

#  What will the count be?
print('User count:', len(deserialized_json))

for key in deserialized_json:
    for nestedKey in key['address_components']:
        print('long_name: ', nestedKey['long_name'])


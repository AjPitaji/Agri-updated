import geocoder

g=geocoder.ip('me')
address = g.geojson

print(address['features'][0]['properties']['state'])
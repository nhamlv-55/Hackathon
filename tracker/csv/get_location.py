import json
from geopy.geocoders import Nominatim

f = open("customers.json", "r")
data = f.read()
f.close()
customers = json.loads(data)

geolocator = Nominatim()
for customer in customers:
	# print customer['address']['street']
	# print customer['address']['city']
	# print customer['address']['state']
	if customer['address']['street'] and customer['address']['state'] and customer['address']['zip']:
		address = customer['address']['street'] + " " + customer['address']['state']
		i = 0
		while i<3:
			try:
				location = geolocator.geocode(address)
				# print location
				if location:
					customer['long'] = location.longitude
					customer['lat'] = location.latitude
				else:
					customer['long'] = "-1"
					customer['lat'] = "-1"
				print customer['_id']
				i=100
			except:
				i+=1
	else:
		customer['long'] = "-1"
		customer['lat'] = "-1"

out = open("customer_with_geo.json", "w")
out.writelines(json.dumps(customers))
out.close()
import json

with open('input.json') as json_data:
	data = json.load(json_data)
	print (type(json_data))
	print (type(data))
	for r in data['Employee']:
		print (r ['City'])

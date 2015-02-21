import json

data = {
	'units' : 20,
	'price' : 322.00
}

into_json = json.dumps(data)

print(into_json)
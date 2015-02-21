import json
json_string = '{"country":"Netherlands","continent":"Europe"}'

data = json.loads(json_string)
print("Country: {0}, Continent: {1}".format(data["country"], data['continent']))
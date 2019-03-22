import json
with open('points.json') as json_data:
    d = json.load(json_data)
    json_data.close()

print type(d)
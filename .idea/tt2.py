import json
with open('points.txt') as json_data:
    d = json.load(json_data)
    json_data.close()

print d
import json
import dateutil


data = json.load(open("4106stops.json"))

for a in data['body']:
    print(a)
import json

with open('countries.json', 'r') as f:
    countries_dict = json.load(f)

for countries in countries_dict:
    print("Name: " + countries['name'])

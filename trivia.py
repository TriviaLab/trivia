import json

with open('countries.json', 'r') as f:
    countries_dict = json.load(f)

for countries in countries_dict:
    print("Name: " + countries['country'])

with open('states.json', 'r') as f:
    states_dict = json.load(f)

for states in states_dict:
    print("Name: " + states['name'])
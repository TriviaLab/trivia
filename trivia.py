import json
import random

random_int = random.randint(1, 2)
if random_int == 1:

    with open('countries.json', 'r') as f:
        countries_dict = json.load(f)

    for countries in countries_dict:
        print("Country: " + countries['country'] + "     City: " + countries['city'])

if random_int == 2:
    with open('states.json', 'r') as f:
        states_dict = json.load(f)

    for states in states_dict:
        print("State: " + states['name'] + "     City: " + states['capital'])
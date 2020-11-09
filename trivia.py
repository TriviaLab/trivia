import json
import random

random_int = random.randint(0, 1)

if random_int == 0:

    def random_country():
        with open('countries.json', 'r') as f:
            countries_dict = json.load(f)
            random_index = random.randint(0, len(countries_dict)-1)
            return countries_dict[random_index]['country']
            
    print("Which city is the capital of " + random_country() + "?")
    #print("The capital is " + random_country_capital())

if random_int == 1:
    with open('states.json', 'r') as f:
        states_dict = json.load(f)

    for states in states_dict:
        print("State: " + states['name'] + "     Capital: " + states['capital'])
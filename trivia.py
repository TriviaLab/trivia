import json
import random

random_int = random.randint(0, 1)

if random_int == 0:
    with open("states.json", "r") as f:
        states_dict = json.load(f)
    
        random_index = random.randint(0, len(states_dict['states'])-1)

        print("Which city is the capital of " + states_dict["states"][random_index]["name"] + "?")	
        input()
        print(states_dict["states"][random_index]["capital"])
    
if random_int == 1:
    with open("countries.json", "r") as f:
        countries_dict = json.load(f)
    
        random_index = random.randint(0, len(countries_dict['countries'])-1)

        print("Which city is the capital of " + countries_dict["countries"][random_index]["country"] + "?")	
        input()
        print(countries_dict["countries"][random_index]["city"])
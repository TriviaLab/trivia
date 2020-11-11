import json
import random

with open("states.json", "r") as read_file:
    states_dict = json.load(read_file)
    
    random_index = random.randint(0, len(states_dict['states'])-1)

    print("Which city is the capital of " + states_dict["states"][random_index]["name"] + "?")	
    input()
    print(states_dict["states"][random_index]["capital"])
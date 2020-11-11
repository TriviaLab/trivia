import json
import random

with open("states.json", "r") as read_file:
    states_dict = json.load(read_file)
    
    random_index = random.randint(0, len(states_dict['states'])-1)

    print(random_index)

    print("State: ", states_dict["states"][random_index]["name"])
    print("Capital: ", states_dict["states"][random_index]["capital"])
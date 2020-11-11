import json

with open("states.json", "r") as read_file:
    states_dict = json.load(read_file)
    
    print("State: ", states_dict["states"][0]["name"])
    print("Capital: ", states_dict["states"][0]["capital"])
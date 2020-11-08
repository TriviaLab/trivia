import json

with open('/data/data/com.termux/files/home/trivia/states.json', 'r') as f:
    states_dict = json.load(f)

for states in states_dict:
    print("Name: " + states['name'])

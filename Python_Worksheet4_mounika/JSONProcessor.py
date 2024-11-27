import json


# Function to load JSON data from a file
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to print JSON data in a pretty format
def print_json(data):
    print(json.dumps(data, indent=4))

# Function to update the 'man_of_the_match' field based on highest score
def update_man_of_the_match(data):
    # Find the player with the maximum score
    max_score_player = max(data, key=lambda x: x['player_score'])
    # Set 'man_of_the_match' to True for the player with the highest score
    max_score_player['man_of_the_match'] = True
    return data

# Function to write the updated data back to a JSON file
def write_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
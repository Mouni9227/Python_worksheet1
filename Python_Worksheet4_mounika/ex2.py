"""Create a module, JSONProcessor. It should contain functions for loading JSON data from an external file and printing
JSON data. The JSON file should contain following player details. Create a JSON file with this information.
{
			{
				“player_name”: “Shubham”
				“player_email”: “shubham@abc.org”
				“player_score: 45
				“man_of_the_match”: false
			},
			{
				“player_name”: “Rohit”
				“player_email”: “rohit@abc.org”
				“player_score: 75
				“man_of_the_match”: false
			},
			{
				“player_name”: “Virat”
				“player_email”: “virat@abc.org”
				“player_score: 100
				“man_of_the_match”: false
			}
]
}
Load this file into a dictionary using the JSON module.  Set the man_of_the_match field to True for a player who has scored
the maximum score among all players. Write back this information into a new JSON file.

"""


import json

import JSONProcessor

# Load the original JSON data
player_data = JSONProcessor.load_json('players.json')

# Print the original data
print("Original Player Data:")
JSONProcessor.print_json(player_data)

# Update the man_of_the_match field
updated_data = JSONProcessor.update_man_of_the_match(player_data)

# Print the updated data
print("\nUpdated Player Data (with man_of_the_match):")
JSONProcessor.print_json(updated_data)

# Write the updated data to a new JSON file
JSONProcessor.write_json('updated_players.json', updated_data)

































import json

# Create a dictionary of Indian states and capitals
indian_states = {
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Delhi": "New Delhi",
    "Kerala": "Thiruvananthapuram",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar"
}

# Write the dictionary to a JSON file
with open("indian_states.json", "w") as json_file:
    json.dump(indian_states, json_file, indent=4)

print("Data has been written to indian_states.json")

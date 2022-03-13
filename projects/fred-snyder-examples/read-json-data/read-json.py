import json

# Read JSON data into the datastore variable
with open("data.json", 'r') as f:
    datastore = json.load(f)

# Use the new datastore datastructure
print(datastore["foo"])

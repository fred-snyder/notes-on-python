import os
import json
from pprint import pprint
# ! FIX this import. "extract" moved to "helpers" directory
from extract import json_extract

airtable_data_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
filename = "Projecten_2020_08_19_14_53_13.json"

# read JSON from disk
with open(os.path.join(airtable_data_folder, filename)) as f:
    data = json.load(f)


# Find every instance of `name` in a Python dictionary.
# TODO: finish this
'''
project_names = json_extract(data, 'project_name')
filenames = json_extract(data, 'filename')
print(project_names)
print(filenames)
print(filenames[0])


records = a list of tuples = ['id', 'fields', 'createdTime']
fields = dictionary
'''

for i in data['records']:
    for i in i['fields'].get('project_name'):
        print(i)

    for key, val in i['fields'].items():
        pass
        # print(key, val)
        # print("\n")
        # print(key[0]['project_name'])

print(data.get('project_name'))

for i, key in enumerate(data['records']):
    print(i, ": ", key['id'], "\n")

    for key,value in key['fields'].items():
        print("KEY: ", key, "VAL: ", value)
        # print(key['project_name'])

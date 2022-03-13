#!/usr/bin/env python

"""
This script downloads JSON data from Airtable and stores it in the "airtable_data" folder.
"""

import os
import pathlib
import requests
import json
import arrow # arrow displays the time in the same format as Hugo frontmatter
from dotenv import load_dotenv
from pprint import pprint
from typing import Iterator
load_dotenv()

# project imports
# ! FIX: fix imports. Python files moved to "helpers" directory
import frontmatter_variables
import bcolors # CLI character colors

# get current date in Hugo SSG compatible format
now = arrow.now().to('Europe/Amsterdam').format('YYYY-MM-DDTHH:mm:ssZZ') # year, month, day, etc sorts well
print("LOG: Date today:", now)

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_BASE_NAME = "Projecten"

# requests headers dictionary
headers = {
	"Authorization": "Bearer " + AIRTABLE_API_KEY,
}

# requests parameters tuple
params = (
	('maxRecords', '3'),
	('view', 'Grid view'),
)

# retrieve data from Airtable
# request get takes `headers` and `params` as parameters
request_url = "https://api.airtable.com/v0/" + AIRTABLE_BASE_ID + "/" + AIRTABLE_BASE_NAME
r = requests.get(request_url, headers=headers, params=params)
pprint(r.json())

# construct the airtable_data folder path from the location of this script
airtable_data_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

# check if "data" folder exists
def check_existence_folder(path, foldername):
	folder = pathlib.Path(path)
	if folder.exists() == True:
		print("LOG: `check_existence_folder`: Folder exists: " + str(folder) )
		return True
	else:
		print(bcolors.WARNING + "LOG: `check_existence_folder`: " + str(folder) + " does not exists" + bcolors.ENDC)

# create a filename for the json data
def json_filename(filename):
	# print("LOG: JSON Timestamp: ", timestamp_now)
	timestamp = arrow.now().to('Europe/Amsterdam').format('YYYY_MM_DD_HH_mm_ss')
	return (filename + "_" + timestamp + ".json")

# write JSON to new file in data folder
def write_json_to_disk(path, filename, data):
	with open(os.path.join(path, filename), "w") as outfile: 
			outfile.write( data )

# use json.dumps to "pretty" format the json and write to disk
json_data = json.dumps(r.json(), indent=4, sort_keys=False)
# create filename for the JSON data
filename = json_filename(AIRTABLE_BASE_NAME)

def success(status):
	if status == "success":
		print(bcolors.OKBLUE + "Download succesfull" + bcolors.ENDC)
		return True
	else:
		print(bcolors.FAIL + "Download failed" + bcolors.ENDC)
		return False

def main():
	if check_existence_folder(airtable_data_folder, "airtable_data"):
		write_json_to_disk(airtable_data_folder, filename, json_data)
		success("success")
	else:
		print(bcolors.WARNING + "LOG: JSON file not written to disk" + bcolors.ENDC)
		success("error")

# execute main
main()

# end of script

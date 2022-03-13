"""
Verify if a certain application is running.
"""

import subprocess
import csv

appname = "maya.exe"

p_tasklist = subprocess.Popen('tasklist.exe /fo csv',
stdout=subprocess.PIPE,
universal_newlines=True)

pythons_tasklist = []

for p in csv.DictReader(p_tasklist.stdout):
    if p["Image Name"] == appname:
        print(p)
        pythons_tasklist.append(p)

if len(pythons_tasklist) > 0:
	print("{} is running".format(appname))

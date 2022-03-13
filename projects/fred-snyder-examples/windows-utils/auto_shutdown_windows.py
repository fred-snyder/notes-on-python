"""
Automatically shutdown windows after a user defined time period
"""

import subprocess
from time import sleep

print("")
print("Auto Shutdown Windows")
print("=====================")
print("")
seconds = float(raw_input("Specify time in minutes: ")) * 60.0
print("")
print(">>> Computer will force shutdown automatically in %s minutes") %(seconds/60.0)
sleep(seconds)
subprocess.call(["shutdown", "/s", "/f"])

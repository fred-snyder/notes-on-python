"""
Robocopy backup script

In "execute_robocopy" replace the string "drive" with the actual drive letter.
Also, replace the path-placeholders with the actual paths.

Author: Fred Snyder
"""

# modules
import string
from glob import glob
from sys import argv
from sys import exit
from subprocess import call


# variable for the script name
script_name = "robocopy_backup.py"


# variable to turn on  the robocopy /L (list files only) flag
if argv[1].lower() == 'test': # argv[0] is always the name of the script
	test_run_robocopy = True
else:
	test_run_robocopy = False

# variable to include/exclude certain folders
exclude_folders = False


# Get the drive letter as user input
drive_letter = input("External backup drive letter: ")
print('Is this correct? Drive: ' + drive_letter)
confirm_drive_letter = input("Y/N ")
if confirm_drive_letter.lower() == 'n':
	exit('Wrong drive letter.')


# function that runs the robocopy command
def execute_robocopy():
	# robocopy variables
	source =  "drive:\\path\\to\\folder"
	destination = drive_letter + ":\\path\\to\\folder"
	logPath = drive_letter + ":\\backup.log"
	log = "/LOG:" + logPath

	# folders which are excluded from backup
	# WARNING: no trailing slashes behind directories
	if exclude_folders == True:
		excludeDirs = ['drive:\\foldername', 'drive:\\$RECYCLE.BIN', 'drive:\\System Volume Information']
	else:
		excludeDirs = []

	# files which are excluded from backup
	excludeFiles = ["pagefile.sys", "thumbs.db", ".DS_Store", ".Spotlight-V100", ".Trashes" ]
	# check if certain file exists
	if len(glob("drive:\\filename*")) > 0:
		excludeTEMP = glob("drive:\\filename*")[0]
		excludeFiles.append(excludeTEMP[3:])

	# create command list for subprocess.call
	command = ["robocopy", source, destination, "/MIR"]
	# check if script is running in test mode
	if test_run_robocopy == True:
		command.extend(["/L"])
	command.extend([log])
	command.extend(["/XD"] + excludeDirs)
	command.extend(["/XF"] + excludeFiles)
	
	# call the subprocess
	call(command)

execute_robocopy()

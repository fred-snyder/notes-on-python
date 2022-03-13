"""
This script creates a backup of all files in a folder which have a specific extension.
It creates an archive and appends the current date to the filename.
"""

from os import listdir
from datetime import date
import zipfile


# create zip archive containing only a certain file-type
def create_zip_archive():
	path = 'd:\\path\\to\\folder\\'
	extension = '.ext'
	zipfile_name = 'd:\\path\\to\\folder\\filename_' + str(date.today()) + ".zip"
	zip = zipfile.ZipFile(zipfile_name, 'w')
	# list all files in the specified path
	for i in listdir(path):
		# check if file has the desired extension
		if i.endswith(extension):
			try:
				# write file to archive
				zip.write(path + i)
			except IOError:
				print("An I/O error occured")
	# close and save the archive
	zip.close()


create_zip_archive()

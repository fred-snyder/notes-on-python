#!/usr/bin/env python

import os
import pathlib
import arrow # arrow displays the time in the same format as Hugo frontmatter

# project imports
# ! FIX this import. Moved to "helpers" directory
import frontmatter_variables

now = arrow.now().to('Europe/Amsterdam').format('YYYY_MM_DD_HH_mm_ss')

# process and map airtable/hugo frontmatter variables
frontmatter_variables.title = "Test title"
frontmatter_variables.date = "some date"
frontmatter_variables.draft = "some draft status"
frontmatter_variables.author = "Fred"
frontmatter_variables.image= "not yet"
frontmatter_variables.description= "This is a test markdown file"
frontmatter_variables.categories = ["wiki"]
frontmatter_variables.tags = ["test-article"]
frontmatter_variables.post_type = "project"

content_markdown = '''
This is a test post.
'''

content_list = [
    '---', # frontmatter seperator
    'variableName_test: ',
    'datemodified: ' + now,
    '---', # frontmatter seperator
    content_markdown
    ]

content_merge = os.linesep.join(content_list)

# create a markdown file
print(content_merge)

# create a filename for the json data
# TODO regex only azAz_- characters
def postname_to_filename(postname):
    filename = postname.replace(" ", "_")
    print(filename)
    return (filename + ".md")

# write markdown to Hugo content folder
def write_markdown_to_disk(path, filename, data):
	with open(os.path.join(path, filename), "w") as outfile: 
			outfile.write( data )

hugo_content_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "content")

post_filename = postname_to_filename("Test output")
write_markdown_to_disk(hugo_content_folder, post_filename, content_merge)

# end of script

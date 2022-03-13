# this file is a description for how the Airtable fields map to the Hugo frontmatter
# this could be a way to make the script more modular
# because there is seperate data structure which describes the relationship between the two applications

'''
options:

{ key: value }
{ hugo_frontmatter_variable_name: airtable_field_name }
hugo_frontmatter_variable_name = airtable_field_name

edge case:
- the hugo `type` frontmatter variable is also reserved keyword in Python. Is this a problem?

'''

'''
TODO


or!! create a simple .toml file which maps the reletionship
volgende stap een script die over de mapper heen loopt
en de markdown genereert
'''
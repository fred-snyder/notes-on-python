'''
Context managers
A mechanism for the automatic setup and teardown of resources
In other words: they facilitate the proper handling of resources.

When to use context managers: anytime you're managing resources.
Examples: database connections, read/write files
'''

# https://book.pythontips.com/en/latest/context_managers.html

# without context manager
f = open('with-open-context-manager-example-file.txt', 'r')
file_contents = f.read()
f.close()

# with context manager
with open('with-open-context-manager-example-file.txt', 'r') as f:
    file_contents = f.read()

# the write variant
with open('with-open-context-manager-example-file.txt', 'w') as f:
    f.write('Hello world')

# the equivalent of above
'''
f = open('with-open-context-manager-example-file.txt', 'w')
try:
    f.write('Hello world')
finally:
    f.close()
'''

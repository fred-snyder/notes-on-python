import sqlite3

# make connection to sqlite
conn = sqlite3.connect('emaildb.sqlite')
# a cursor allows Python-code to execute SQL commands in a database session
cur = conn.cursor()

# make sure we start with a clean database
cur.execute('DROP TABLE IF EXISTS Counts')

# create a new empty table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')


# open the data file
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

# loop over lines in the data
for line in fh:
    # only work on lines that start with "From: "
    if not line.startswith('From: '): continue

    # extract email
    pieces = line.split()
    email = pieces[1]
    email_domain = email.split('@')
    email_domain = email_domain[1]
    #print(email_domain)

    # query databse for the count of that email
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email_domain,))

    # get the result of that query
    row = cur.fetchone()
    if row is None: # if the row is empty add 1 new count to that row
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email_domain,))
    else: # if the row is not empty increment the existing value with 1
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email_domain,))
    # commit the changes to the database
    conn.commit()
    

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# execute the query in the string above
# and print out every line of the result
# the result is a list
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# close the database connection
cur.close()

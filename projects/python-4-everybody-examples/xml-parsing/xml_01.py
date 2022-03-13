import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_134196.xml

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #address = input('Enter location: ')
    address = 'http://py4e-data.dr-chuck.net/comments_134196.xml'
    if len(address) < 1: break

    # url = urllib.parse.urlencode(address)
    url = address
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')

    sum_collecter = 0

    for i in counts:
        sum_collecter += int(i.text)

    print(sum_collecter)
    break

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_134196.xml

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = "http://py4e-data.dr-chuck.net/comments_134197.json"
url_handle = urllib.request.urlopen(url, context=ctx)
data = url_handle.read()

info = json.loads(data.decode())
print('User count:', len(info))

sum_of_counts = 0

for i in info['comments']:
    print('Name', i['name'])
    print('Count', i['count'])
    sum_of_counts += int(i['count'])

print(sum_of_counts)

'''import re
re.search()
re.findall()

text = 'lorem ipsum'
re.search('^lor', text)

line = 'lorem ipsum 1995 sidade'
re.findall('[0-9]+', line)
'''

import re
handle = open('regex_sum_134192.txt')

result = []
for line in handle:
	result += re.findall('[0-9]+', line)

sum_ = int()
for i in result:
	sum_ += int(i)

print(sum_)

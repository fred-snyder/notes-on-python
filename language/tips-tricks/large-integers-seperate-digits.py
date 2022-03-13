'''
To make large numbers more readable
you can use underscore to seperate digits
'''

intiger1 = 10_000_000_000
# intiger1 = 10000000000

intiger2 = 10_000_000
# intiger2 = 10000000

intiger_sum = intiger1 + intiger2

print(f'{intiger_sum:_}')
print(f'{intiger_sum:,}')

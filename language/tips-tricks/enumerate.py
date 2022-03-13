# enumerate

brand_list = ['Apple', 'Dell', 'HP', 'Lenovo']
for counter, value in enumerate(brand_list):
    print(counter, value)

# start count at 1
for counter, value in enumerate(brand_list, 1):
    print(counter, value)

counter = 0
for value in brand_list:
    print(counter, value)
    counter += 1

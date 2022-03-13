# condition = False
condition = True

x = 1 if condition else 0
# two alternatives
x = (1 if condition else 0)
x = (1 if condition == True else 0)

print(x)

# the same as above
if condition:
    x = 1
else:
    x = 0

print(x)

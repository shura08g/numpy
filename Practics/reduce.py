from functools import reduce

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# multiplier = lambda x, y: x * y


def multiplier(x, y):
    return x * y

result1 = reduce(multiplier, data)
print(result1)

product = 1
for x in data:
    product = product * x

print(product)

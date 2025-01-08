'''find the product of all the numbers in a list using reduce()
numbers=[1,2,3,4]
output=24'''


from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)


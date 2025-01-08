'''find the factorial of a number using reduce()and lambda 

input=5
output=120'''

from functools import reduce

# Input
n = 5
result = reduce(lambda x, y: x * y, range(1, n + 1))
print(result)  

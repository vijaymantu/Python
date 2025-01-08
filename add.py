'''add 10 to each number in a list 
input=[1,2,3]
output=[11,12,13]'''

numbers = [1, 2, 3]
res = list(map(lambda x: x + 10, numbers))
print(res)

'''sconcatenate list of string into a single string using reduce()
list=["welcome","to","skyllx"]
output=["welcometoskyllx"]'''

from functools import reduce

string=["welcome","to","skyllx"]
string = reduce(lambda a,b : a+b,string)
print(string)



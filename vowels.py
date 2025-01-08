#filter out all the vowels from  a list of characters
list=['a','b','e','i','o','u','z']

res=list(filter(lambda x:x in "aeiou",list))
print("this output is from filter")
print("the output is from filter function",res)


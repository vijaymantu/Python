'''find longest word in a list of a string using a reduce()
list=["apple","bananan","cat","elephant"]'''

from functools import reduce

words = ["apple", "banana", "cat", "elephant"]
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest_word)

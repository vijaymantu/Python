def merge_dicts(dict1, dict2):
    return dict1 | dict2
dict1 = {'a': 5, 'b': 6}
dict2 = {'c': 7, 'd': 8}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)

# This defines a function called merge_dicts that takes two arguments,
#  dict1 and dict2. These are the two dictionaries that you want to merge.
# Inside the function, the line return dict1 | dict2 
# merges the two dictionaries using the | operator

# dict1 has keys 'a' and 'b' with values 1 and 2
# dict2 has keys 'c' and 'd' with values 3 and 4

# Inside the function, dict1 | dict2 merges the two dictionaries into a new dictionary.
# This calls the merge_dicts function and passes dict1 and dict2 as arguments.

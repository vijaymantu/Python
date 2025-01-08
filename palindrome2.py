def is_palindrome(input_string):
    return input_string == input_string[::-1]
input_str = "shivu"
if is_palindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# The function is_palindrome takes a string input_string as an argument.
# input_string[::-1] is used to reverse the string.
# reverses the string using Python's slicing technique.
# The function then compares the original string (input_string)
#  to its reversed version (input_string[::-1]).
# If they are equal, it means the string is a palindrome 
# (i.e., it reads the same forwards and backwards), and the function returns True.
# If they are not equal, it means the string is not a palindrome,
#  and the function returns False.
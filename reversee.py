def reverse_string(input_string):
    return input_string[::-1]   #[start:end:steps]
result = reverse_string("hello")
print(result)  


# The function takes one parameter: input_string,
#   which is expected to be a string that you want to reverse.

# The -1 tells Python to step through the string backward,
# effectively reversing it.

# So, [::-1] returns a new string 
# that is the reversed version of input_string.

# This line calls the reverse_string function 
# with the string "Skyllx" as the argument.

# Finally, the print(result) line 
# prints the reversed string "xllykS" to the console.




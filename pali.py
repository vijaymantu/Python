'''lambda fuction to check if number is palindreome
input:121
output:true'''

# Lambda function to check if a number is a palindrome
is_palindrome = lambda n: str(n) == str(n)[::-1]
input_number = 125
output = is_palindrome(input_number)
print(output)

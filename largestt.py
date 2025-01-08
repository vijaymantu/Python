def largest_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
result = largest_of_three(100,200,300)
print(result) 

# The function largest_of_three takes three arguments:
#  num1, num2, and num3.

# It compares the numbers using if and elif conditions:
# If num1 is greater than or equal to both num2 and num3,
#  it returns num1.
# If num2 is greater than or equal to both num1 and num3,
#  it returns num2.
# If neither of the above conditions is true,
#  it returns num3 (since it must be the largest).
# The function is called with the numbers 10, 25, and 15, and 
# the largest number (25) is printed.


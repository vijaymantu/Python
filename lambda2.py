
#lambda function to find the maximum of two numbers
max=lambda(x,y,z : x if x>y and x>z else y if y>z else z)
print("the maximum value is :",max(5,10,12))
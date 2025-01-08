#count the frequency of characters in a string.


def frequnecy_character(name):
    frequnecy={}
    for char in name:
        if char in frequnecy:
            frequnecy[char]+= 1
        else:
            frequnecy[char]=1
    for char,count in frequnecy.items():
        print(char,'_',count)
name=input("enter a string:")
count_char(name)




#print("Hello,world!")
 #Write a program to take the user's name as input and print "Hello, [name]!".

# name=input("enter name:")
# print(  "Hello, ",name,"!")

#  Write a program to add two numbers provided by the user.

# a=int(input("enter first number:"))
# b=int(input("enter second number:"))
# c=a+b
# print(c)

#Write a program to find the square of a number entered by the user.

# a=int(input("enter a number:"))
# print("Squre : ",a**2)

# Write a program to swap two numbers without using a temporary variable.

# a=10
# b=20
# print("a:",a,"b:",b)
# # temp=a
# # a=b
# # b=temp
# a,b=b,a
# print("a:",a,"b:",b)


#6. Write a program to calculate the sum, difference, product, and quotient of two numbers.

# def input_name():
#     user_input_name=input("Enter a name: ")
#     return user_input_name
# def output_name(user_output_name):
#     print("Your Name: ",user_output_name)

# input_name_variable=input_name()
# output_name(input_name_variable)   



















# print("welcome to SkyllX")

# name = input()
# print(name)

# for nameId in range(0,3):
#     name = input("Enter the name : ",) 
#     print("Name at",nameId+1," - ",name)
    # 1st iteration
    # indexs => 0,1,2,3

# list = ['Arun','Shivu',"Mahanthesh","Vishal"]
# print(list[4])
# for names in list :
#     print(names)

# Q: Using range() to iterate Over numbers
    # 1, 2, 3, 4, 5
    # range(firstIndex,lastIndex) -> firstIndex,....,lastIndex-1
    # range(0,5) -> 0, 1, 2, 3, 4
    # range(5,10)-> 5, 6, 7, 8 , 9
    # range(0,6) -> 0, 1,2,3,4,5
# for i in range(1,6) :
#     print(i)
# for i in range(0,5) :
#     print(i+1)

# Q: Iterate over a string
    # SkyllX -> S, k, y, l, l, X

#str="skyllx"
#for chars in str :
    #print(chars )

# Iterating with indexes
# names = ['Arun','Shivu',"Mahanthesh","Vishal"]
# 0 : Arun
# 1 : Shivu
# 2 : Mahanthesh
# 3 : Vishal
# # (enumerate)
# for index, name in enumerate(names) :
#     print(index,' : ',name)

# continue(skipping the iteration) & break(breaking the loop)
# for i in range(0,10) :
#     if(i == 0 or i == 3):
#         continue
#     if(i==7):
#         break
#     print(i)

# Nested for loop
# for i in range(2):
#     for j in range(3):
#         print("i = ",i," j = ",j)

#Q:write a python program to print all the elements of a list,one by one

#names=["arun","vishal","shivu","mantu"]
#for name in names:
    #print(name)

#create a program that prints numbers from 1 to 10 using for loop
#given a string print each character of the string an a new line
#write a program to calculate sum of all the numbers in a list using for loop


#for i in range(1,11):
    #print(i)

#str="mantu"
#for i in str:
    #print(i)

# sum = 0 => 0+1=1 => 1+2=>3....
# sum = 0
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     sum = sum + i
# print(sum)
    

#use a for loop to print only even numbers between 1 and 20

# for i in range(1,21):
#     if(i%2==0):
#         print(i)

# for i in range(1,21):
#     if i%2!= 0:
#         print(i)

# for i in range(5,11):
#     print(i)

#printing even numbers 

# for i in range(1,21):
#     if i %2==0:
#         print(i)

# for i in range(1,21):
#     if i%2!=0:
#         print(i)

# cars=["celerio","swipt","crysta","creta"]
# for car in cars:
#     print(car)

#using for loop with else

# for i in  range(1,6):
#     print(i)
# else:
#     print("loop completed")

# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j,end="")
#     print()

# for a in range(1,6):
#     for b in range(5,11):
#         print(a*b,end="")
#     print()

# for i in range(1,15):
#     if i==10:
#         break
#     print(i)

# for i in range(1,10):
#     if i==8:
#         break
#     print(i)

# for i in range(1,10):
#     if i==7:
#         continue
#     print(i)

# for i in range(1,31):
#     if i%2==1:
#         print(i)

# phones=["vivo","oppo","samsung","iphone"]
# for phone in phones:
#     print(phone)

# for char in "realme":
#     print(char)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_sum=0
# for num in numbers:
#     if num%2==0:
#         even_sum+=num
# print("sum of even numbers:",even_sum)

# numbers=[2,4,6,8,10]
# for num in numbers:
#     if num==5:
#         print("number 5 is found!")
#         break
#     else:
#         print("number 5 is not found in list.")

# numbers=[1,2,3,4,5]
# largest=numbers[0]
# for num in numbers:
#     if num>largest:
#         largest=num

# print("the largest number is :",largest)

# function which return reverse of a string

# def isPalindrome(s):
#     return s == s[::-1]
# s = "aru"
# res=isPalindrome(s)
# if res:
#     print("given string is palindrome")
# else :
#     print("given string is not palindrome")
s="madam"
if s == s[::-1]:
    print("given string is palindrome")
else :
    print("given string is not palindrome")

# str=input("Enter a string:")
# new = ''.join(i for i in str if i.isalnum())
# if str.lower() == new[::-1].lower():
#     print("The word is pure")
# elif new.lower() == new[::-1].lower():
#     print("The phrase holds symmetry")
# else:
#     print("The word lacks balance")

#check if number is even or odd
# a = int(input("enter the number"))
# if a%2 == 0:
#        	print("the given number is even number")
# else:
# 	    print("given number is odd number")

# r=input("enter a string:")
# rev=""
# for i in r:
# 	rev=i+rev
# print(rev)
	
# r=input("enter a sting")
# rev=""
# for i in r:
#     rev=i+rev
# print(rev)

#calculate sum of digits of a number

# number=int(input("enter a number")) #123
# sum=0
# def sumofdigits(n,sum): 
#     if n<10:
#         return n+sum
#     return sumofdigits(n//10,n%10+sum) 
#                                     #sumofdigits(123//10=12,123%10+0=3)
#                                     #sumofdigits(12//10=1,12%10+3=5)
# print(sumofdigits(number,0))

# numbers = input("enter a numnber") #123
# def sum_of_digits(numbers):
#     return sum(int(digit) for digit in str(numbers))
#                                     # 1,2,3
# print(sum_of_digits(numbers))


# r=input("enter a number")  #123
# rev="" #none
# for i in r: #1
#     rev=i+rev #1+none
#     #1 + none => 1
#     #2 + 1 => 21
#     #3 + 21 => 321
# print(rev) #321  

# a=50
# b=20
# c=10
# if a>b:
#     print("a is grater then b")
# else:
#     print("b is grater then a")


# a=int(input("enter first25 number:"))
# b=int(input("enter secend number:"))
# c=int(input("enter third number:"))
# def largest_num(a,b,c):
#     return max(a,b,c)
# print(largest_num(a,b,c))

# hello goodmorning!!!
# Here I'm wrote the python code to solve the problem to find the largest number of three numbers.

# For that, we are declaring 4 int type variables a, b, c and largest.
# And for variable a, we initializing a value as 80.
# And for variable b, we initializing a value as 50.
# And for variable c, we initializing a value as 10.
# a=80
# b=50
# c=10
# largest=int()  #initializes the variable largest with an integer type(default value 0)
# print(type(largest),' - ',largest)  #prints the type of largest and its current value is 0.
# def check_largest_number(a,b,c) :  #Using def keyword, a function named check_largest_number is defened, by taking 3 parameters : a,b and c.
#    rgest=a       
        
#         return largest
#     elif b>=a and b>=c: # Then I'm using the "Else If Condition" to assign variable b to variable largest and to return variable largest if variable b is greter then or equal to both variables a and c. Then, if this "Else If Condition"  is true then it will terminate this function moves out of this function, or if this if conditon is false then it will move to next line in the in same function
#         largest=b       
#         return largest  
#     else:
#         largest=c       # Then I'm using the "Else Condition" to assign variable c to variable largest and to return variable largest as I already checked the conditions for variables a and b.
#         return largest  
# print("largest number is: ",check_largest_number(a,b,c))  if a>=b and a>=c:   # Inside that I'm using the "If Condition" to assign variable a to variable largest and to return variable largest if variable a is greter then or equal to both variables b and c. Then, if this if conditon is true then it will terminate this function moves out of this function, or if this if conditon is false then it will move to next line in the  same function
         # Finally I'm calling the check_largest_number function with a,b and c as arguments inside the print() function to print the largest number of three numbers.


# a=0
# b=''
# c=False
# print("a: ",a," type: ",type(a))
# print("b: ",b," type: ",type(b))
# print("c: ",c," type: ",type(c))





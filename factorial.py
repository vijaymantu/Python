num=int(input("Enter number to find the Factorial... "))
def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num * fact(num-1)
print("Factorial Number of",num,"is :",fact(num))

#5*4*3*2*1=120

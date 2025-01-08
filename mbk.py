def calculator(a,b):
	"""calculator()-this is actually performing addition,substraction,multiplication,and division"""
	x=a+b
	y=a-b
	z=a*b
	q=a/b
	return x,y,z,q
res1,res2,res3,res4=calculator(a=10,b=20)
print(res1,res2,res3,res4)
print(calculator,__doc__)

def power_off(num,power):
	return num **power
print(power_off(2,5))
print(power_off(5,2))

def compute(p,t,r):
	si=(p+t+r)/100
	print(si)
compute(10000,2,12.5)

def power_off(num_off,power):
	return num_off**power
res1=power_off(num_off=2,power=5)
res2=power_off(num_off=5,power=2)
print(res1)
print(res2)


def power_off(num_power,power):
	return num_off **power

res1=power_off(2)
print=(res1)
res2=power_off(3)
print=(res2)
res3=power_off(5)
print=res(3)
res=power_off(num=5,power=3)
print(res4)

def pizza_toppings(*toppings):
	print(toppings)
pizza_toppings(toppings:"corn","cheeze","onion","panner","capcicum")


def Submit_details(**details):
	print(details)
Submit_details(name="Rashmika",gender="female",marks="35",city="coorg")

def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)
res=factorial(3)
print(res)

def add(x,y):
	"""Function performs addition"""
	return x+y
def sub(x,y):
	"""Function performs substraction"""
	return x-y
def mul(x,y):
	"""Function performs multiplication"""
	return x*y
def div(x,y):
	"""Function performs division"""
	return x/y

print("addition:",add(5,3))
print("substraction:",sub(5,3))
print("multiplication:",mul(5,3))
print("division:",div(5,3))'''

from turtle import Turtle
t=Turtle()
t.color("red")
t.fillcolor("black")
for i in range(4):
	t.fd(200)
	t.lt(90)


	







	




	


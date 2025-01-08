'''print('mahantesh')
print(10)


a=10
b=20
print(a+b)

a=6.3
print(a)

print(type(a))

b=100000.0000
print(b)
print(type(b))

a='A'
print(a)
print(type(a))

a=True
print(a)
print(type(a))

a=3+4j
print(a)
print(type(a))

a=10
print(type(a))
b=20.0
print(type(b))
c=a+b
print(type(c))

a=10
print(type(a))
b="20"
print(type(b))
c=a+int(b)
print(type(c))

def add():
	a=10
	b=20
	c=a+b
	print(c)
add()


def add():
	a=10
	b=20
	c=a+b
	print(c)
res=add()
print(res)

details={1:"siddu,30,100,ilkal,arj college,rushmika",2:"rushmika,25,35,bangalore,arj college,siddu"}
print(details)
print(details)
print(details[2])

details={3:"mahantesh,23,85,arj college,aishu"}
print(details)


def compute(p,t,r):
	si=(p+t+r)/100
	print(si)

def calculator(a,b):
	x=a+b
	y=a-b
	z=a*b
	q=a/b
	return x,y,z,q
res1,res2,res3,res4=calculator(a=10,b=20)
print(res1,res2,res3,res4)'''


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

def power_off(num,power)
	return_num **power
power(power_off(2,5))
print(power_off(5,2))
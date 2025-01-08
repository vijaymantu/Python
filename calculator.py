def calculator(a,b):
	"""calculator()-this is actually performing addition,substraction,multiplication,and division"""
	x=a+b
	y=a-b
	z=a*b
	q=a/b
	return x,y,z,q
res1,res2,res3,res4=calculator(a=10,b=20)
print(res1,res2,res3,res4)
print(calculator.__doc__)

list=[1,2,3,4,5,6,7,8,9,10]
even_list=[]
for i in list:
	if i%2==0:
		even_list.append(i)
print(list)
print(even_list)


numbers=[1,2,3,4,5,6,7,8,9,10]
even_list=list(filter(lambda i:i % 2 == 0,numbers))
print(numbers)
print(even_list)

numbers=[1,2,3,4,5,6,7,8,9,10]
sq_list[map(lambda i : i*2,list]











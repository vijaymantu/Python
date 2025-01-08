'''use lambda function to create a list of squares  for number 1 to 10
output:[1,4,.....100]'''

# Using lambda to create a list of squares
squares = list(map(lambda x: x**2, range(1, 11)))
print(squares)

#1st :iteration x=1 [1]
#2nd :iteration x=2 [1,4]
#3rd :iteration x= [1,4,9]
#4th :iteration x= [1,4,9,16]
#5th :iteration x= [1,4,9,16,25]
#6th :iteration x= [1,4,9,16,25,36]
#7th :iteration x= [1,4,9,16,25,36,49]
#8th :iteration x= [1,4,9,16,25,36,49,64]
#9th :iteration x= [1,4,9,16,25,36,49,64,81]
#10th :iteration x= [1,4,9,16,25,36,49,64,81,100]










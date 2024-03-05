# What does this piece of code do?
# Answer:Output the sum of 100 random integers between 1 and 10

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil#Import ceil in the math module

progress=0#Assign the initial values of both variables to 0
total_random_numbem_r=0
while progress<100:#Make a judgment in the while loop and enter the loop when progress is less than 100
	progress+=1#progress=progress+1,this loop can be done 100 times
	n = randint(1,10)#n is a random integer ranging from 1 to 10
	total_random_number = total_random_number+n#Add total_random_number to a random integer n


print(total_random_number)#Output the sum of 100 random integers between 1 and 10

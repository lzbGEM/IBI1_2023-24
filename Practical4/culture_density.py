
density=0.05#The initial density is 0.05
a=1#a=1 is used to calculate the day
while density<0.9:#if density <0.9  code into while loop
    density*=2
    a+=1
    print(f'the cell density on day {a} is {density}')#This is formatted output in python
print(f"Cell density does not exceed 0.9 until day {a-1} and will exceed from day {a} onwards")




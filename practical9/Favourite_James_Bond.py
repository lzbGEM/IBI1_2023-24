def James(year):
    age=year+18
    dic={"Roger Moore":range(1973,1986), "Timothy Dalton":range(1987,1994),"Pierce Brosnan":range(1995,2005),"Daniel Craig":range(2006,2021)}
    for j,i in dic.items():#Iterate over the keys and values of the dictionary
        if age in i:
            print(f"This people's favorite James is {j}")
            break
year=int(input("Please input the year in which that	person was born :"))
James(year)


 
	

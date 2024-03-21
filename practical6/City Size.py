uk_cities=[0.56,0.62,0.04,9.7] #konw the population
china_cities=[0.58,8.4,29.9,22.2]

uk_cities.sort()
print(uk_cities)
china_cities.sort()
print(china_cities)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))#can change the figure size
cities_name1=['Edinburgh','Glasgow','Stirling','London']#set a list to store name of x
cities_name2=['Haining','Hangzhou','Shanghai','Beijing']
plt.bar(cities_name1,uk_cities,width=0.3,label='UK')
plt.bar(cities_name2,china_cities,width=0.3,label='CHINA')

plt.xlabel('cities and countries')#name x
plt.ylabel('Population')#name y
plt.title('population in diferent country')#name whole figure
plt.legend()#show the legend
plt.show()
plt.clf()
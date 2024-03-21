import matplotlib.pyplot as plt
activity={'Sleep':8,'Classes':6,'Studying':3.5,'TV':2,'Music':1}
print(activity)


Total=24
other_time=24-sum(activity.values())#calculate the time of 'other'
activity['other']=other_time#add ['other']

a="Sleep"#it can be modified
print(f'Average time of {a} is {activity[a]} hours')

plt.pie(activity.values(),labels=activity.keys(),startangle = 90)#set a pie chart

plt.title('Pie Chart')
plt.show()
plt.clf()



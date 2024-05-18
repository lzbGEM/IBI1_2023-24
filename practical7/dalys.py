import os  # Import the operating system interface module
import pandas as pd  # Import the Pandas library for data analysis
import matplotlib.pyplot as plt  # Import the Matplotlib's pyplot module for plotting graphs
import numpy as np  # Import the NumPy library for numerical calculations

os.getcwd()  # Get the current working directory
os.listdir()  # List all the files and directories in the current working directory

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")  # Read the CSV file into a Pandas DataFrame
print(dalys_data.loc[0:100:10,"DALYs"])  # Print every 10th row up to the 100th row for the 'DALYs' column

Afghanistan_row = []  # Initialize a list to store boolean values for rows where 'Entity' is 'Afghanistan'
for i in dalys_data.loc[:,"Entity"]:  # Iterate over the 'Entity' column in the DataFrame
    if i == "Afghanistan": 
        Afghanistan_row.append(True)  # Append True to the list
    else:
        Afghanistan_row.append(False)  # Otherwise, append False
print(dalys_data.loc[Afghanistan_row,"DALYs"])  # Get the 'DALYs' values for rows where 'Entity' is Afghanistan

china_data = dalys_data.iloc[1140:1170,[0,2,3]]  # Select rows 1140 to 1170 and columns 0, 2, and 3 from the DataFrame
print(china_data)  # Print the selected data for China

Mean = np.array(dalys_data.iloc[1140:1170,3])  # Convert the selected data for China's 'DALYs' into a NumPy array
print(np.mean(Mean))  # Calculate and print the mean of the 'DALYs' for China

print("The dalys of 2019 is smaller than the mean")  

plt.plot(china_data.Year, china_data.DALYs, 'y+')  # Plot the 'Year' vs 'DALYs' for China with yellow plus markers
plt.xticks(china_data.Year, rotation=45)  # Set the x-axis labels to be rotated by 45 degrees for better readability
plt.show()  
plt.clf()  




In_2019 = []  # Initialize a list to store boolean values for rows where 'Year' is 2019
for i in dalys_data.loc[:,"Year"]:  # Iterate over the 'Year' column in the DataFrame
    if i == 2019:  
        In_2019.append(True)  # Append True to the list
    else:
        In_2019.append(False)  # Otherwise, append False
plt.boxplot(dalys_data.loc[In_2019,"DALYs"])  # Create a box plot for the 'DALYs' data where the 'Year' is 2019
plt.show()  
plt.clf()  






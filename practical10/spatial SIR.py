
import numpy as np
import matplotlib.pyplot as plt

beta = 0.3  # Infection probability
gamma = 0.05  # Recovery probability

population = np.zeros((100, 100), dtype=int)

# Randomly choose a point for the initial outbreak
outbreak = np. random . choice (range(100) ,2) 
population [ outbreak [0] , outbreak [ 1 ] ] = 1 

for t in range(100):
    # Find infected points
    infectedIndex = np.where(population == 1)
    
    # Loop through all infected points
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y= infectedIndex[1][i]
    # infect each neighbour with probability beta
    # infect all 8 neighbours (this is a bit finicky, is there a better way?):
    for xNeighbour in range(x-1,x+2):
        for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (Is this strictly necessary?)
            if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                    if population[xNeighbour,yNeighbour]==0:
                        population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        
# Loop through each infected individual in the first row of infectedIndex
    for i in range(len(infectedIndex[0])):
        x, y = infectedIndex[0][i], infectedIndex[1][i]# Get the x (row) and y (column) coordinates of the current infected individual
        if np.random.rand() < gamma:
            population[x, y] = 2


    # Plot the current time step's heatmap
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', vmin=0, vmax=2, interpolation='nearest')
    plt.title(f'Time step {t}')
    plt.show()







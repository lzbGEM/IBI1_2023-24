import numpy as np
import matplotlib.pyplot as plt
N = 10000 # Total population 
S = N - 1  #Initial number of susceptible individuals
I = 1     # Initial number of infected individuals 
R = 0      # Initial number of recovered individuals
beta = 0.3  # Infection rate
gamma = 0.05 # Recovery rate
S_arr = [S]
I_arr = [I]
R_arr = [R] # Arrays to store the values of S, I, R
for i in range(1,1000):  
    infection_rate = beta * (I / N)# Calculate the current infection rate
    new_I = np.random.choice([0, 1], size=S, p=[1 - infection_rate, infection_rate])# Randomly determine new infected individuals based on the infection rate
    S -= new_I.sum()# Update the number of susceptible and infected individuals
    I += new_I.sum()
    new_R = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma])# Randomly determine new recovered individuals based on the recovery rate
    I -= new_R.sum()
    R += new_R.sum()
    # Append SIR to the arrays
    S_arr.append(S)
    I_arr.append(I)
    R_arr.append(R)

time=list(range(1,1001))

# Plot the SIR model using Matplotlib
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(time, S_arr, label='Susceptible')
plt.plot(time, I_arr, label='Infected')
plt.plot(time, R_arr, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.legend()
plt.show()


plt.savefig("SIR.png")#save























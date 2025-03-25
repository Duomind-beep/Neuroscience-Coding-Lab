#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
dt = 0.1  # Time step (ms)
T = 100  # Total simulation time (ms)
time = np.arange(0, T, dt)  # Time vector

# Neuron parameters
V_rest = -65  # Resting membrane potential (mV)
V_th = -50  # Threshold for firing (mV)
V_reset = -70  # Reset voltage after firing (mV)
R = 10  # Resistance (MΩ)
tau = 10  # Membrane time constant (ms)

# Input current (constant for now)
I = 2 

# External input current (nA)

# Initialize membrane potential
V = np.zeros(len(time))  # Array to store voltage over time
V[0] = V_rest  # Start at resting potential

print("Simulation setup complete!")


# In[2]:


# Simulate the neuron’s behavior over time
for t in range(1, len(time)):
    # Update membrane potential using the LIF equation
    dV = (-(V[t-1] - V_rest) + R * I) / tau
    V[t] = V[t-1] + dV * dt  # Euler’s method update

    # Check if the neuron reaches the threshold
    if V[t] >= V_th:
        V[t] = V_reset  # Reset the voltage after firing

print("Simulation complete!")


# In[3]:


# Plot the membrane potential over time
plt.figure(figsize=(10, 5))
plt.plot(time, V, label="Membrane Potential (V)")
plt.axhline(y=V_th, color='r', linestyle='--', label="Threshold (-50 mV)")
plt.axhline(y=V_rest, color='g', linestyle='--', label="Resting Potential (-65 mV)")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential (mV)")
plt.title("Leaky Integrate-and-Fire Neuron Simulation")
plt.legend()
plt.show()


# In[ ]:





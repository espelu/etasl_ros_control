#!/usr/bin/env python

import numpy as np
import time
import matplotlib
from matplotlib import pyplot as plt

t = time.time()
G = 9.81 #import readings from zero out bias
phi = np.pi/4 # import from tf or make a script to calculate
theta = np.pi/4 # import from tf or make a script to calculate


def spher2cart(): #G, phi, theta

    fx = G * np.sin(theta) * np.cos(phi)
    fy = G * np.sin(theta) * np.sin(phi)
    fz = G * np.cos(theta)

    print (fx,fy,fz)
    
    return[fx,fy,fz]

forces = np.array([1,3,2,5,1,5])
print(forces)
n = 5
vektor = np.zeros((6,n))
print(vektor)

vektor = np.append(vektor, [1,2,3,4,5,6])
print(vektor)
vector = np.append(vektor,forces)
print(vector)
vector = vector.reshape(7,6)
print(vector)
vector[1,2]=3
print(vector)
n=vector[1].size
print(n)
#####OK####
# plt.plot(vector[6])
# plt.xlabel('Time (seconds)')
# plt.ylabel('fx')
# plt.show()


######OK######
def importData(): #force_x, force_y,  n, t
    global netft_matrix
    netft_matrix = np.zeros((6,n))
    for i in range(n): # 6 rows of fx,fy...
        netft_matrix [0,i] = vector[5,i] #fx
        netft_matrix [1,i] = vector[5,i] #fy
        netft_matrix [2,i] = vector[5,i]
        netft_matrix [3,i] = vector[5,i]
        netft_matrix [4,i] = vector[5,i]
        netft_matrix [5,i] = vector[6,i]
        pass
    print(netft_matrix)
    #return netft_matrix
    pass

      
  

def sumVector(matrix):
    sum = np.zeros((6,1))
    std_dev = np.zeros((6,1))
    var = np.zeros((6,1))
    for i in range(6):  
        sum[i] = np.mean(matrix[i])
        std_dev[i]= np.nanstd(matrix[i])
        var[i] = np.var(matrix[i])
        
        pass
    print("mean av vektoren - ", sum)
    print("standard deviation - ", std_dev)
    print("variance av vektoren - ", var)

# spher2cart() 
importData()     
print(netft_matrix) 
sumVector(netft_matrix)
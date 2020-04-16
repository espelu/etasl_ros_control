import numpy as np

G = 9.81 #import readings from zero out bias
phi = np.pi/4 # import from tf or make a script to calculate
theta = np.pi/4 # import from tf or make a script to calculate


def spher2cart(): #G, phi, theta

    fx = G * np.sin(theta) * np.cos(phi)
    fy = G * np.sin(theta) * np.sin(phi)
    fz = G * np.cos(theta)

    print (fx,fy,fz)
    
    return[fx,fy,fz]

spher2cart()    
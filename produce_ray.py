import numpy as np
import math

# This function returns an array of randomly generated photons depending on the angular
# position of the sun (theta, phi) and the maximal size (R) of the optical configuration

# The returned value is a matrix of points and a matrix of angles of the lines intersecting these points

def produce_ray(theta, phi, R, trials):
    

# We first generate the dimensions of the plane needed to shade the optical
# configuration

    extra_width = 0.00925031
    M = R + extra_width * 2

    x_init = np.random.uniform(-M, M, trials)
    z_init = np.random.uniform(-M, M, trials)

    vecs = np.stack((x_init, np.full(trials, R), z_init))
# Then we rotate them to be in the right direction
    R_phi = np.array([[1, 0, 0],
            [0, math.cos(phi), math.sin(phi)],
            [0, -math.sin(phi), math.cos(phi)]])
    R_theta = np.array([[math.cos(theta), -math.sin(theta), 0],
            [math.sin(theta), math.cos(theta), 0],
            [0, 0, 1]])


    vecs = R_theta @ R_phi @ vecs

# Next we generate an array of angles for the lines

    theta_init = np.random.uniform(theta - 0.0265, theta + 0.0265, trials)
    phi_init = np.random.uniform(phi - 0.0265, phi + 0.0265, trials)
        
    angles = np.stack((theta_init, phi_init), axis = 0)

    return (vecs, angles)










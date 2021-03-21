from sage.all import *
import numpy as np
import math

# The following is an example of functional sage code. It initializes a polynomial ring,
# then generates an ideal from it

#P = PolynomialRing(RR, 3, 'x')

#var('x0 x1 x2')

#I= Ideal(P, [4 + 3*x0 + x0**2, 1 + x0**2])

#To get generators just use I.gens()


# The purpose of this function will be to generat implicitizations for the lines generated in
# produce_ray

def imp_ray(vec, angle):
    P = PolynomialRing(RR, 3, 'x')
    var('x0 x1 x2')
    n = vec[0].size
    ideals = []
    for i in range(n):
        gens = []
        v = [vec[0, i], vec[1, i], vec[2, i]]
        theta = angle[0, i]
        phi = angle[1, i]
        variab = [x0, x1, x2]
        p = [math.sin(phi)*math.cos(theta), math.sin(phi) * math.sin(theta), math.cos(phi)]
        if p[0] * p[1] * p[2] != 0:
# we derive an implicitization from the parameterization p + tv. If v has no nonzero components the 
# computation is straightforward, otherwise we have to check which components are 0
            gens.append(p[1]/p[0]*x0 - p[1]/p[0]*v[0] - v[1] - x1)
            gens.append(p[2]/p[0]*x0 - p[2]/p[0]*v[0] + v[2] - x2)
        else:
            counter = 0
            check = 0
            for j in range(3):
                if p[j] == 0:
                    check = j
                    counter += 1
                    gens.append(variab[j] - v[j])
            if counter == 1:
                a = (check - 1) % check
                b = (check + 1) % check
                gens.append(p[b]/p[a] * variab[a] - p[b]/p[a] * v[a] + v[b] - variab[b])
        I = Ideal(P, gens)
        ideals.append(I)
    return ideals






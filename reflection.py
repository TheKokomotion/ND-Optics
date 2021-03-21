from sage.all import *

# this function will reflect an implicit equation about a plane. The inputs are imp the implicit function, N the normal vector of the plane, R the ring everything is over, and p the point of intersection of imp and the plane.

def reflection(imp, N, p, R):
    N = matrix(R, N)
    n_mat = N.transpose() * N
    ref = matrix(R, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]) - 2*n_mat
    var('x0 x1 x2')
    variab = vector(R, [[x0], [x1], [x2]])
    point = vector(R, [[p[0]], [p[1]], [p[2]]])
    newv = ref * (variab - point) + point
    return imp(x0 = newv[0], x1 = newv[1], x2 = newv[2])

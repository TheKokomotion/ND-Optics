from sage.all import *



# This code will be used to generate the implicit function and normal for the tangent plane to a point on a variety given the point and the implicit function corresponding to that point.

def gen_plane(p, f):
    var('x0 x1 x2')
    fx = f.diff(x0)(x0 = p[0], x1 = p[1], x2 = p[2])
    fy = f.diff(x1)(x0 = p[0], x1 = p[1], x2 = p[2])
    fz = f.diff(x2)(x0 = p[0], x1 = p[1], x2 = p[2])
    Df = matrix([fx, fy, fz])
    K = Df.right_kernel().basis()
    normal = K[0].cross_product(K[1])
    p_eq = normal[0] * (x0 - p[0]) + normal[1] * (x1 - p[1]) + normal[2] *(x2 - p[2])
    return (p_eq, normal)


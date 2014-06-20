import numpy as np
from math import cos, sin, radians

# Code for week 2 exercises
def get_rotational_matrix(theta):
    ''' Return the rotational matrix with angle theta in degrees'''
    theta = radians(theta)
    R = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
    return R

def get_transformational_matrix(x, y, theta):
    ''' Return the transformational matrix for a robot moving in
    the direction (x,y) with bearing theta
    M = [ R t ]
        [ 0 1 ]
    t = [x, y]^T
    R = [cos -sin]
        [sin cos]
    '''
    R = get_rotational_matrix(theta)
    M = np.append(R, [[x], [y]], 1)
    M = np.append(M, [[0, 0, 1]], 0)
    return M
    
print get_rotational_matrix(90)
print get_transformational_matrix(2, 3, 90)
M1 = get_transformational_matrix(1, 2, 45)
M2 = get_transformational_matrix(-4, 2, 45)
print M1
print M2
# note: np.dot is different from *
print np.dot(M1, M2)
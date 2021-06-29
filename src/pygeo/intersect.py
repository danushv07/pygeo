from .objects import Ray, Sphere, Point, Vector, Triangle
import numpy as np
import math


def _intersect_ray_with_sphere(a,b):
    """ Function for intersection of Ray and Sphere"""
    x = np.dot(a._direction,a._direction)
    y = 2 * np.dot((a._direction),(a._origin - b._centre))
    z = np.dot((a._origin - b._centre),(a._origin - b._centre)) - b._radius**2
            
    discr = y**2 - 4*x*z #check discriminant
    if discr < 0.0:
        return False
    elif discr == 0.0: #only one intersection
        t = -y / (2*x)
        sp_cls = []
        for e,f in zip(a._origin,a._direction):
            sp_cls.append(e+t*f)
        return Point(sp_cls) 
    else: # two intersection points
        t_1 = (-y + np.sqrt(discr))/ (2*x)
        t_2 = (-y - np.sqrt(discr))/ (2*x)
        
        if(t_1 > 0):
            if(t_2 >0):
                sp_1_cls = []
                sp_2_cls = []
                for c,d in zip(a._origin,a._direction):
                    sp_1_cls.append(c+t_1*d)
                for i,j in zip(a._origin,a._direction):
                    sp_2_cls.append(i+t_2*j)
                return Point(sp_1_cls),Point(sp_2_cls)
            else:
                sp_1_cls = []
                for c,d in zip(a._origin,a._direction):
                    sp_1_cls.append(c+t_1*d)
                return Point(sp_1_cls)
        else:
            sp_2_cls = []
            for i,j in zip(a._origin,a._direction):
                    sp_2_cls.append(i+t_2*j)
            return Point(sp_2_cls)

def _intersect_ray_with_triangle(x,y):
    """Fucntion for ray triangle intersection(Möller-Trumbore algorithm)"""
    edge1 = y.v1 - y.v0 #edge 1
    edge2 = y.v2 - y.v0 #edge 2
    determinant = np.dot(edge1,(np.cross(x._direction,edge2)))
    f = 1/determinant
    s = x._origin - y.v0
    t = f * np.dot(edge2,(np.cross(s,edge1)))
    
    if determinant < (10**(-6)): #back facing triangle
        return False
    
    elif math.fabs(determinant) < (10**(-6)): # Ray triangle parallel
        return False
    
    else:
        u = f * np.dot(s,(np.cross(x._direction,edge2)))
        if(u < 0 or u > 1):
            return False
        else:
            v = f * np.dot(x._direction,(np.cross(s,edge1)))
            if(v<0 or (u+v) > 1):
                return False
            else:
                return Point((u,v,t))

def _intersect(x,y):
    """Function to select the appropriate intersection function"""
    if (isinstance(x,Ray) and isinstance(y,Sphere)): 
            return _intersect_ray_with_sphere(x,y)
    elif (isinstance(x,Ray) and isinstance(y,Triangle)):
            return _intersect_ray_with_triangle(x,y)
    else:
        return False
    
 

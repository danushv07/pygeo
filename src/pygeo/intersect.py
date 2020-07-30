
from .objects import Ray, Sphere, Point, Vector
import numpy as np

def _intersect_ray_and_sphere(a,b):
    """ Function for intersection of Ray and Sphere"""
    x = np.dot(a.dir,a.dir)
    y = 2 * np.dot((a.dir),(a.p0 - b.cp))
    z = np.dot((a.p0 - b.cp),(a.p0 - b.cp)) - b.rp**2
            
    discr = y**2 - 4*x*z #check discriminant
    if discr < 0.0:
        return False
    elif discr == 0.0: #only one intersection
        t = -y / (2*x)
        sp_cls = []
        for e,f in zip(a.p0,a.dir):
            sp_cls.append(e+t*f)
        return Point(sp_cls) 
    else: # two intersection points
        t_1 = (-y + np.sqrt(discr))/ (2*x)
        t_2 = (-y - np.sqrt(discr))/ (2*x)
        
        if(t_1 > 0):
            if(t_2 >0):
                sp_1_cls = []
                sp_2_cls = []
                for c,d in zip(a.p0,a.dir):
                    sp_1_cls.append(c+t_1*d)
                for i,j in zip(a.p0,a.dir):
                    sp_2_cls.append(i+t_2*j)
                return Point(sp_1_cls),Point(sp_2_cls)
            else:
                sp_1_cls = []
                for c,d in zip(a.p0,a.dir):
                    sp_1_cls.append(c+t_1*d)
                return Point(sp_1_cls)
        else:
            sp_2_cls = []
            for i,j in zip(a.p0,a.dir):
                    sp_2_cls.append(i+t_2*j)
            return Point(sp_2_cls)
    


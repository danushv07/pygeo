import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Point({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """This class represents a ray"""
    def __init__(self,origin_p,dir_r):
        self.p0 = np.array(origin_p)
        self.dir = np.array(dir_r)
        
    def __repr__(self):
        return f"Ray origin ({self.p0.tolist()}) and  Ray direction({self.dir.tolist()})"
        
     
    def __eq__(self,other):
        if isinstance(other, Ray):
            return np.array_equal(self.p0,other.p0) and np.array_equal(self.dir,other.dir)
        return False 


class Sphere:
    """A Sphere class with centre and radius"""
    def __init__(self,centre,radius):
        self.cp = np.array(centre)
        self.rp = np.array(radius)
    
    def __repr__(self):
        return f"Sphere centre ({self.cp.tolist()}) and  Sphere radius({self.rp.tolist()})"
        
     
    def __eq__(self,other):
        if isinstance(other,Sphere):
            return np.array_equal(self.cp,other.cp) and np.array_equal(self.rp,other.rp)
        return False 

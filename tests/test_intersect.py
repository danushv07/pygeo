from pygeo.intersect import  (_intersect_ray_with_sphere,
                              _intersect,
                              _intersect_ray_with_triangle)
from pygeo.objects import Ray, Sphere,Triangle, Point, Vector


# intersect function
def test_given_ray_sphere_return_one_point_():
    assert(_intersect(Ray((0,0,0),(1,1,0)),Sphere((1,1,1),1)) == Point((1,1,0))) is True

def test_given_ray_triangle_return_intersection_point():
    assert(_intersect_ray_with_triangle(Ray((5,2,5), (0,0,-1)), Triangle(((0,0,0),(10,0,0),(5,10,0)))) == Point((0.4,0.2,5))) is True

def test_given_ray_vector_return_false():
    assert(_intersect(Ray((2,0,1),(0,-1,0)), Vector((1,2,3))) is False) is True

# Ray_sphere_intersection
def test_given_ray_sphere_same_origin_return_one_point_intersection():
    assert (_intersect_ray_with_sphere(Ray((0,0,0),(0,-1,0)),Sphere((0,0,0),5)) == Point((0,-5,0))) is True

def test_given_ray_sphere_no_intersection_return_false():
    assert (_intersect_ray_with_sphere(Ray((0,0,0),(0,1,0)),Sphere((5,5,5),5)) is False) is True

def test_given_ray_sphere_return_tangent_intersection():
    assert (_intersect_ray_with_sphere(Ray((0,0,0),(1,1,0)),Sphere((1,1,1),1)) == Point((1,1,0))) is True

# Ray_triangle_intersection
def test_given_ray_triangle_no_intersection_return_false():
    assert(_intersect_ray_with_triangle(Ray((0,0,0), (1,1,0)),Triangle(((1,0,0),(0,1,0),(0,0,1)))) is False) is True

def test_given_ray_triangle_no_intersection_return_false():
    assert(_intersect_ray_with_triangle(Ray((0,0,0), (1,1,0)), Triangle(((1,1,0),(3,1,0),(2,0,1)))) == Point((0,0,1))) is True    

from pygeo.intersect import (
    
    _intersect_ray_with_sphere,
    
)
from pygeo.objects import Ray, Sphere, Triangle

# _intersect_ray_with_sphere
def test_given_ray_sphere_same_origin_return_one_point_intersection():
    assert (_intersect_ray_and_sphere(Ray((0,0,0),(0,-1,0)),Sphere((0,0,0),5)) == Point((0,-5,0))) is True

def test_given_ray_sphere_no_intersection_return_false():
    assert (_intersect_ray_and_sphere(Ray((0,0,0),(0,1,0)),Sphere((5,5,5),5)) is False) is True

def test_given_ray_sphere_return_tangent_intersection():
    assert (_intersect_ray_and_sphere(Ray((0,0,0),(1,1,0)),Sphere((1,1,1),1)) == Point((1,1,0))) is True

# Imported modules
from geometry10.square import get_s_triangle, get_s_rectangle
from geometry10.volume import get_v_cone, get_v_sphere

class Geometry:
    def __init__(self, s_triangle, s_rectangle, v_cone, v_sphere):
        self.s_triangle = s_triangle
        self.s_rectangle = s_rectangle
        self.v_cone = v_cone
        self.v_sphere = v_sphere


s_triangle = get_s_triangle(5)
s_rectangle = get_s_rectangle(15, 5)
v_cone = get_v_cone(2, 10)
v_sphere = get_v_sphere(7)

geometry = Geometry(s_triangle, s_rectangle, v_cone, v_sphere)

print(geometry.s_triangle)
print(geometry.s_rectangle)
print(geometry.v_cone)
print(geometry.v_sphere)

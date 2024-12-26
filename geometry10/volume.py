from math import pi

'''The volume of a cone'''
def get_v_cone(radius, height) -> float:
    v = 1 / 3 * pi * radius ** 2 * height
    return v

'''The volume of a sphere'''
def get_v_sphere(radius) -> float:
    v = 4 / 3 * pi * radius ** 3
    return v

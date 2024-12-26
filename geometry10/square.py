'''The area of an isosceles right triangle'''
#
def get_s_triangle(side) -> float:
    s = 1 / 2 * side ** 2
    return s

'''The area of a rectangle'''
def get_s_rectangle(side, side2) -> float:
    s = side * side2
    return s

import math

# ---- Cube ----
# a = side of cube
def cube_csa(a):
    return 4 * a * a   # 4 side faces

def cube_tsa(a):
    return 6 * a * a   # all 6 faces

def cube_volume(a):
    return a ** 3


# ---- Cuboid ----
# l = length, b = breadth, h = height
def cuboid_csa(l, b, h):
    return 2 * h * (l + b)   # side faces only

def cuboid_tsa(l, b, h):
    return 2 * (l*b + b*h + l*h)

def cuboid_volume(l, b, h):
    return l * b * h


# ---- Cylinder ----
# r = radius, h = height
def cylinder_csa(r, h):
    return 2 * math.pi * r * h

def cylinder_tsa(r, h):
    return 2 * math.pi * r * (r + h)

def cylinder_volume(r, h):
    return math.pi * r**2 * h


# ---- Cone ----
# r = radius, h = height, l = slant height
def cone_csa(r, l):
    return math.pi * r * l

def cone_tsa(r, l):
    return math.pi * r * (r + l)

def cone_volume(r, h):
    return (1/3) * math.pi * r**2 * h


# ---- Sphere ----
def sphere_csa(r):
    return 4 * math.pi * r**2

def sphere_tsa(r):
    return 4 * math.pi * r**2   # same as CSA

def sphere_volume(r):
    return (4/3) * math.pi * r**3


# ---- Hemisphere ----
def hemisphere_csa(r):
    return 2 * math.pi * r**2   # curved part only

def hemisphere_tsa(r):
    return 3 * math.pi * r**2   # curved + base

def hemisphere_volume(r):
    return (2/3) * math.pi * r**3
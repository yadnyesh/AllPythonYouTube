import math

def volume_of_sphere(r):
    """ Returns the volume of a Sphere with radius r."""
    volume = (4/3) * math.pi * r**3
    return volume

print(volume_of_sphere(2))
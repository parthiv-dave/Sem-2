import numpy as np
import math

def cartesian_to_polar(points):
    x = points[:, 0]
    y = points[:, 1]
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return np.column_stack((r, theta))

N = 10
points_cartesian = np.random.rand(N, 2) * 10 - 5

points_polar = cartesian_to_polar(points_cartesian)

print("Cartesian Coordinates:")
print(points_cartesian)
print("\nPolar Coordinates:")
print(points_polar)
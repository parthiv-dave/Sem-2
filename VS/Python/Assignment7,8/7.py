import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def angle_with_x_axis(self):
        return math.degrees(math.atan2(self.y, self.x))

    @staticmethod
    def distance(v1, v2):
        return math.sqrt((v2.x - v1.x) ** 2 + (v2.y - v1.y) ** 2)

    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y

    @staticmethod
    def cross_product(v1, v2):
        return v1.x * v2.y - v1.y * v2.x

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross_product(v1, v2):
        return Vector3D(v1.y * v2.z - v1.z * v2.y,
                        v1.z * v2.x - v1.x * v2.z,
                        v1.x * v2.y - v1.y * v2.x)

dimension = int(input("Enter dimension (2 or 3): "))

if dimension == 2:
    x1, y1 = map(float, input("Enter first 2D vector (x y): ").split())
    x2, y2 = map(float, input("Enter second 2D vector (x y): ").split())
    v1, v2 = Vector2D(x1, y1), Vector2D(x2, y2)
    print("Magnitude of first vector:", v1.magnitude())
    print("Distance between vectors:", Vector2D.distance(v1, v2))
    print("Dot Product:", Vector2D.dot_product(v1, v2))
    print("Cross Product:", Vector2D.cross_product(v1, v2))

elif dimension == 3:
    x1, y1, z1 = map(float, input("Enter first 3D vector (x y z): ").split())
    x2, y2, z2 = map(float, input("Enter second 3D vector (x y z): ").split())
    v1, v2 = Vector3D(x1, y1, z1), Vector3D(x2, y2, z2)
    print("Magnitude of first vector:", v1.magnitude())
    print("Dot Product:", Vector3D.dot_product(v1, v2))
    cross = Vector3D.cross_product(v1, v2)
    print("Cross Product:", (cross.x, cross.y, cross.z))

else:
    print("Invalid dimension")

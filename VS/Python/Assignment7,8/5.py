import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

shape_type = input("Enter shape (rectangle/circle): ").strip().lower()

if shape_type == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    rect = Rectangle(length, width)
    print("Rectangle - Area:", rect.area(), "Perimeter:", rect.perimeter())

elif shape_type == "circle":
    radius = float(input("Enter radius: "))
    circle = Circle(radius)
    print("Circle - Area:", circle.area(), "Perimeter:", circle.perimeter())

else:
    print("Invalid shape type")

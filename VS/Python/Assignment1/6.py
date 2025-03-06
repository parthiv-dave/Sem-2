import math

points = []
print("Enter 10 coordinates : ")
for i in range(10):
    x, y, z = map(float, input(f"Enter coordinates for point {i+1} (x y z): ").split())
    points.append((x, y, z))

nearest = []
for i in range(10):
    min_dist = float('inf')
    nearest_point = None
    for j in range(10):
        if i != j:
            dist = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2 + (points[i][2] - points[j][2]) ** 2)
            if dist < min_dist:
                min_dist = dist
                nearest_point = points[j]
    nearest.append((points[i], nearest_point))

print("\nNearest Neighbors:")
for pair in nearest:
    print(f"Point {pair[0]} → Nearest: {pair[1]}")
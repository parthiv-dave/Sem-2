import math

def count_squares(A, B):
    return math.floor(math.sqrt(B)) - math.ceil(math.sqrt(A)) + 1

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(count_squares(A, B))

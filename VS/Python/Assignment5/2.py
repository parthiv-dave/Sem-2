def max_chocolate_pieces(K):
    return (K // 2) * (K - K // 2)

T = int(input())
for _ in range(T):
    K = int(input())
    print(max_chocolate_pieces(K))
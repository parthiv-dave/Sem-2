def make_magic_square(n):
    if n % 2 == 1:
        magic_square = [[0] * n for _ in range(n)]
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[i][j] = num
            next_i, next_j = (i - 1) % n, (j + 1) % n
            if magic_square[next_i][next_j]:
                i = (i + 1) % n
            else:
                i, j = next_i, next_j
    elif n % 4 == 0:
        magic_square = [[(i * n) + j + 1 for j in range(n)] for i in range(n)]
        for i in range(n // 4):
            for j in range(n // 4):
                magic_square[i][j] = n * n + 1 - magic_square[i][j]
                magic_square[i][n - 1 - j] = n * n + 1 - magic_square[i][n - 1 - j]
                magic_square[n - 1 - i][j] = n * n + 1 - magic_square[n - 1 - i][j]
                magic_square[n - 1 - i][n - 1 - j] = n * n + 1 - magic_square[n - 1 - i][n - 1 - j]
        for i in range(n // 4, 3 * n // 4):
            for j in range(n // 4, 3 * n // 4):
                magic_square[i][j] = n * n + 1 - magic_square[i][j]
    else:
        k = n // 2
        A = make_magic_square(k)
        B = [[A[i][j] + k * k for j in range(k)] for i in range(k)]
        C = [[A[i][j] + 2 * k * k for j in range(k)] for i in range(k)]
        D = [[A[i][j] + 3 * k * k for j in range(k)] for i in range(k)]
        magic_square = []
        for i in range(k):
            magic_square.append(A[i] + C[i])
        for i in range(k):
            magic_square.append(D[i] + B[i])
        for i in range(k):
            if i == k // 2:
                for j in range(1, k // 2):
                    magic_square[i][j], magic_square[i + k][j] = magic_square[i + k][j], magic_square[i][j]
            else:
                for j in range(k // 2):
                    magic_square[i][j], magic_square[i + k][j] = magic_square[i + k][j], magic_square[i][j]
    return magic_square

def print_magic_square(square):
    n = len(square)
    for row in square:
        print(" ".join(f"{num:3d}" for num in row))
    print(f"Magic constant: {n * (n * n + 1) // 2}\n")

N = int(input("Enter a No. to make Magic Square = "))
magic_square = make_magic_square(N)
print_magic_square(magic_square)
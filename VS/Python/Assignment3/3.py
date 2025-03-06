def utopian_tree_height(N):
    height = 1
    for cycle in range(1, N + 1):
        if cycle % 2 == 1:
            height *= 2
        else:
            height += 1
    return height

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        N = int(data[i])
        print(utopian_tree_height(N))

if __name__ == "__main__":
    main()
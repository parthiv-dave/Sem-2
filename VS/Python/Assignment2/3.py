T = int(input("Enter no. of inputs = "))
for _ in range(T):
    N = int(input())
    count = sum(1 for i, digit in enumerate(str(N)) if digit != '0' and N % int(digit) == 0)
    print(count)
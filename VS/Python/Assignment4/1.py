def love_letter(s):
    operations = 0
    n = len(s)
    
    for i in range(n // 2):
        operations += abs(ord(s[i]) - ord(s[n - i - 1]))
    
    return operations

T = int(input())
for _ in range(T):
    s = input().strip()
    print(love_letter(s))

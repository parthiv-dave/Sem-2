def ispangram(s):
    s = s.lower()
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return "pangram" if alphabet.issubset(set(s)) else "not pangram"

s = input().strip()
print(ispangram(s))
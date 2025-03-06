word = input("Enter a word: ")
result = ''.join([char.upper() if i % 2 else char.lower() for i, char in enumerate(word)])
print(result)
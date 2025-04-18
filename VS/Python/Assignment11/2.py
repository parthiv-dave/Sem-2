import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper_case = s.str.upper()

lower_case = s.str.lower()

lengths = s.str.len()

print("Original Series:\n", s)
print("\nUppercase:\n", upper_case)
print("\nLowercase:\n", lower_case)
print("\nLengths:\n", lengths)

mod_classes = {i: [] for i in range(5)}
for num in range(1, 10001):
    mod_classes[num % 5].append(num)

for mod in mod_classes:
    print(f"Equivalence class for mod {mod}: {mod_classes[mod][:10]} ... {mod_classes[mod][-10:]}") 

all_numbers = []
for nums in mod_classes.values():
    all_numbers.extend(nums)

print("Validity Check:", set(all_numbers) == set(range(1, 10001)))
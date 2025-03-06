import random
random_list = [random.choice([0,1]) for _ in range(100)]
def max_zero(lst):
    max_count=0
    current_count=0
    for num in lst:
        if num==0:
            current_count+=1
            max_count=max(max_count,current_count)
        else:
            current_count=0
    return max_count
print(max_zero(random_list))
import math

def prefibo(n):
    a,b=0,1
    while a+b<n:
        a,b=b,a+b
    return a,b
def isfibo(n):
    if math.sqrt(m+4) == int(math.sqrt(m+4)) or math.sqrt(m-4) == int(math.sqrt(m-4)) :
        a,b = prefibo(n)
        print(f"Yes it is from fibonacci series {a} + {b}")
    else:
        print("No it is not from fibonacci series")
    
n=int(input("Enter a No. = "))
m=5*n*n

isfibo(n)
from sympy import isprime
a,b=map(int,input().split())
for i in range(a,b):
    if isprime(i):
        print(i)
     

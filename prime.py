a=int(input())
# if (a % 1 == 0) and (a % a == 0):
#     print("prime")
# else:
#     print("not prime")
# from sympy import isprime
# if isprime(a):
#     print("prime")
# else:
#     print("not prime")
count = 0
for i in range(1,a+1):
    if a%i == 0:
        count += 1
if count == 2:
    print("Prime")
else: 
    print("Not Prime")

n=int(input())
a=0
b=1
print("fib :",a,b,end=" ")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
 
#print()
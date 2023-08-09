# a=int(input())
# fact=1
# for i in range(1,a+1):
    # fact=fact*i
# print(fact)
#djksbjfsjbajfbdjsbagjfvdbsfjdabskjfbjdsabfjbadshb

num=int(input())
factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

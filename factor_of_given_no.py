num=int(input("enter no. to find factor"))

result=[]
for i in range (1,num//2):
    if num%i==0:
        result.append(i)

result.append(num)
print(result)

#time complext O(n/2)->O(n)
#space complexity=O(k)
print("-----------optimum solution---------------")
from math import sqrt
numm=int(input("enter no. to find factor"))

result=[]
for i in range (1,int(sqrt(numm))+1):
    if numm%i==0:
        result.append(i)
        if numm//i !=i:
            result.append(numm//i)

result.sort()
print(result)

#time complexity O(srqt(n))

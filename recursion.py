#print abhay four time without using loop
print("print abhay n time without using loop")
count=0
def fun(n):
    if n==4:
        return
    print("abhay")
    n+=1
    fun(n)

fun(count)
#time complexity O(n)
#space complexityO(n)
#print x n time 
print("print x n times ")
def func(x,n):
    if n==0:
        return
    print(x)
    func(x,n-1)

func(12,4)

#SUM OF 1 TO N number
print("sum of 1 to n numbers")
def summ(sum,i,n):
    if i>n:
        print(sum)
        return
    summ(sum+i,i+1,n)
summ(0,1,4)

print("factorila od the given number")
def fact(f,n):
    if n<0:
        print("factorial is not possile")
    elif n==0:
        print(f)
        return
    fact(f*n,n-1)
fact(1,4)

print("optimized way of finding factorial")
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)
print(factorial(5))

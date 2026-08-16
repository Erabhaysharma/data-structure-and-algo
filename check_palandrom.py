#if your input is pelendrom then return true else return false
n=1234

def check_pelendrom(n):
    num=n
    result=0
    while num>0:
        l_d=num%10
        result=(result*10)+l_d
        num=num//10
    return n==result
check_pelendrom(n)
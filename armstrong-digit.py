num=int(input("enter no. to check armstrong"))
n=num
nod=len(str(n))
print(nod)
total=0

while n>0:
    digit=n%10
    total+=digit**nod
    n=n//10
if total==num:
    print(f" total {total} and given no {num} this is armstrong")
else:
    print("given no. is not armstrong")

#tme complesxi(log base10 n)
#space compexity O(1)
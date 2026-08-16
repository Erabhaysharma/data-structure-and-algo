a=2
b=False
c=3.33
d=4+2j
e=a+b+c+d
print(f"e={e}",type(e))


print("------------------OPRATOR TESTING-----------------------")

a=13.0
b=4
c=a/b
e=a//b
f=8%3

print(f"result of / is {c} and result of // is {e} \n rement of 3%8 is {f}")

print("diffrent sign")
x=17
y=-3
p=x%y
print(p)

num=[1,2,3,4]
for n in num:
 if n<3:
    
    num.remove(n)
print(num)
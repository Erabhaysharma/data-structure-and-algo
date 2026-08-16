l1=[1,2,3]
l3=l1
l2=[1,2,3]
print(id(l1))
print(id(l2))
print(l1 is l3)
print(l1 is not l2)

print("--------membership oprator-----------------")
x="abhay"
print('a' in x)

l4=['abhay','kumar','sharma']
print('abhay' in l4)
print('kumar' not in l4)
print('sharma' in l4)
print("--------ternary  oprator-----------------")
a,b=10,20
x=20
x=2 if a<b else 10
print(x)

x,y,z=10,20,9
p=x if x>z and x>z else b if x>z else z
print(p)
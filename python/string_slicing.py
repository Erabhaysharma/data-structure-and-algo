s='i am abhay kumar'
print(s[0:10]) #op-> i am abhay

#slicing with step value

print(s[0:8:2]) #op->ia b this is becuse skiping one value after pring a value
 
print(s[0:17:3]) #op-> imbyur -> this is becuse skipping 2 value after printing one vale like i skip skip m skip skip b skip skip y skip skip u skip skip r


## eliminating  first perameter

st='abc'*3  #op-> abcabcabc

print(st[:9:3])

#eliminateing both first and second perameter

print(st[::4]) #skipping 3 vale after printing a value

#skipping any perameter allowed in the python

print(st[::3])
print(st[1::3])

list=[1,2,3,4,5,6,7]
print(len(list))

print(list[0:7:2])

str='string'

print(str[6:0:-1])

#reverse the string using slicing
print(str[::-1])
print(s[::-1])
print(list[::-1])


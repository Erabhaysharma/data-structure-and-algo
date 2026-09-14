# % formatying
name='abhay'

print('my name is %s'%name)

#multiple variable are also alloewd in formation

city='ambala'
print('my name is %s and i am from %s'%(name,city))

# if you want too inclue integer vale you can use %d for floting %f
age=23
hight=5.9

print('my name is %s i am %d year old my heigh %f and i am from %s'%(name,age,hight,city))

# str.format() function
print('my name is {} and i from {}.'.format(name,city))
#we can also use index as refrence 
print(' my name is {0} and i from {1}'.format(name,city))

#to improve the readablity we can also use keyfor 
a='anurag'
b='madhubbni'
print("my name is{name} and i from {city}".format(a=name,b=city))

#f string formation

print(f'my  ame is {name} and i live in {city}')

#call to method aslo can be used in f string format

print(f'my name is {name.upper()} and i live in {city.upper()}')

#for better readablity multiline f-string can be used

intro=f'my name is {name}.'
print(intro)

# output can lso includein the trin
a=20
b=10
print(f' the sum of 10 sn 20 is {a+b}')

#escaping curly braces
print(f" the result of {a+b} is 30{{{a+b}}}")
# the comprehension list help use to reduce the line of code for smae work

#here the tardiotional method to make new list using exixting list applying some condition
names=['ram','saam','sita','gita','git','gata','anup']

a_name=[]
for name in names:
    if 'r' in name:
        a_name.append(name)
print(a_name) # o/p=['abhay','aanand,'adarsh',anup]

#similar task can be doone using comprehension list

s_name=[name for name in names if 'g' in name]
print(s_name)#o/p=[sam,sidarth]
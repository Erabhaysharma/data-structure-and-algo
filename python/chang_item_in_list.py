# this file will show how you can change single and multiple items in the list
list=['abhay','kumar',1]

list[2]='sharma'
print(list)

#changeing multiple item in the list
# here we can use slicng method
list2=['a','b',1,2,3]
print('before changing multiple item',list2)
x=len(list2)
list2[2:x]=['h','a','y']
print("after chageing multiple item",list2)

#inserting new item in the list
#for inserting new item in the list we can use insert() method
list3=['dr.','abhay','kumar',3]
list3.insert(len(list3)-1,'sharma')
print(list3)

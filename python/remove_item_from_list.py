#there are various method to remove the item from the list
#1st remove()
li=["ram",'sam','sita','lakhn']
li.remove('sam')
print(li)

#pop() helps to remove item from the specified index

li2=['gita','sita','nita']
x=li2.pop(2)
print(f"{x} is removed item from {li2}") #pop method not only remove the item from the list it alos retun the removed item so 
                                            #later we can use it


#del  keyword we can delete specified item from the list or also abel to delete entire list

li3=[1,2,3]
del li3[0]
print(li3)
del li # it will delete the whole list

#clear() this method help us to empty the list meant not list is delteted but it will be empty
li4=[1,2,3,4,5]
print("list before using cler method",li4)
li4.clear()
print('after using cler method',li4)

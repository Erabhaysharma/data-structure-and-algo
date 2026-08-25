# for adding element in the list we have mainly three method
#1st-> append(): this help to add a item at the end of the list
#2nd-> insert(): this help us to add element at the specific position of the list
#3rd-> extend(): this method help use to extend the exixting list by adding another list

list=[1,2,3,4]
print(list)

print(" add 5 in the list at end ")
list.append(5)
print(list)
my_list=[4,3,2,1]
print(my_list)
print(" add 5 at the first position of the list")
my_list.insert(0,5)
print(my_list)

my_list2=[1,2,3,4,5]
my_list3=[6,7,8,9]
print(f"extend the {my_list2} by adding {my_list3}")
my_list2.extend(my_list3)
print(my_list2)
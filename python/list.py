#this file contain all abut list
# 1. define or create list
list_num=[1,2,3,4,5,6] 
list_char=["a","b","c"]
multi_d_type_list=["a","abhay",1,1.2]

print("here all type of list that can be define",list_num, list_char,multi_d_type_list)
print("this lis is a single demesnnol list")

#acessing elements in s-d list

my_list1=[1,2,3,4]
#through positive indexing
my_list1[0] #1
my_list1[2]#2 and similar for acessing 3 and four

#through negtive indesing its espessly user when we dont know lenghth of list and wnat to acess lat element

my_list1[-1]# 4
my_list1[-2]# 3

# multi dmensinol list 
# the multi d list is the list that contain another list in a list e.g

my_list2=[1,[2,3,4],"abhay",[10,20,30]]

# let we want to acess 2 
#so the code for that
print(my_list2[1][0])
#similar if you wnat to acess 30
print(my_list2[-1][2])

#q. let we have given list
my_list3=[[1,2,3],[['a','b','c'],4,5]]
print(my_list3)
print("acess the b from the list")
print(my_list3[1][0][1])

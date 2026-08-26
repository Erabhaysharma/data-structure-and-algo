n=int(input("enter the length of the list you want"))
nums=[]
for i in range(n):
    x=int(input(f'enter the {i} elemnt of the list'))
    nums.append(x)
print(f"you final list is {nums}")

#using this method we can take list as the input from the user

#list input uisng split method

list=input('enter a no. of wnat to store in the list').split()
print(list)

#aceepting list using split and for lopp method 

length=int(input("enter the length of the list"))

list=input('enter the elements of the list:').split()
for i in range(0,length):
    list[i]=int(list[i])
print(f"your final typecated list is :{list}")
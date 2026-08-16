print("reverse list using for loop")

list=[1,2,3,4]

for i in range(len(list)//2):
    list[i],list[len(list)-1-i]=list[len(list)-1-i],list[i]
print(list)


print("reverse list using recursion")
nums=[1,3,4,5,6,8]
def reverse(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right]=nums[right],nums[left]
    reverse(nums,left+1,right-1)
    

reverse(nums,0,len(nums)-1)
print(nums)
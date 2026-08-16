nums=[2,5,2,6,8]
print('accending order')
def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        min_indx=i
        for j in range(i+1,n):
            if nums[j]<nums[min_indx]:
                min_indx=j
        nums[i],nums[min_indx]=nums[min_indx],nums[i]

    return nums

print(selection_sort(nums))
print("deccending order")

def ss(nums):
    n=len(nums)
    
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if nums[j]>nums[min_index]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums
print(ss(nums))

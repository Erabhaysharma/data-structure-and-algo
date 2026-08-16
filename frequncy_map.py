nums=[5,3,4,5,6,8,6,7,4,2,4,5,6,7,1,1]

frq_map={}
for i in range(0,len(nums)):
    if nums[i] in frq_map:
        frq_map[nums[i]]+=1
    else:
        frq_map[nums[i]]=1
print(frq_map)

print(frq_map[5])
#check a given string is palandrom or not using while loop
s=str(input("enter word to check palindrom"))
left=0
right=len(s)-1
def check(s,left,right):
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
print(check(s,left,right))

#time complexity=O(n)
#space complesity O(n)

print("check pelindrom without using loop")
def check_p(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return check_p(s,left+1,right-1)
print(check_p(s,left,right))

#time complexity=O(n)
#space complesity O(n)
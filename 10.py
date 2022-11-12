nums = [-23, 12, -35, 45, 20, 36]
firstnum = nums[0]
secondnum = nums[1]
close = firstnum+secondnum
if close<0:
    close = -close

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        s = nums[i]+nums[j]
        if s<0:
            s = -s
        if close>s:
            firstnum = nums[i]
            secondnum = nums[j]
            close = s
print(firstnum,secondnum)

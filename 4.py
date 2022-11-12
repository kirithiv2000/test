nums = [-1,0,1,2,-1,-4]
array = []
check = set()
for i in range(len(nums)):
    s = set()
    for j in range(i+1,len(nums)):
        k = nums[i]+nums[j]
        if -k in s:
            sortedarray = [nums[i],nums[j],-k]
            sortedarray.sort()
            tupleOfArray = tuple(sortedarray)
            print(check)
            if tupleOfArray in check:
                pass
            else:
                array.append(sortedarray)
                check.add(tupleOfArray)
        s.add(nums[j])
print(array)

def smallerNumbersThanCurrent(nums):
    sortedNums = sorted(nums)
    smaller = [0] * len(nums)
    d = {}

    # Create dict {val : #smaller than val}
    for i in range(len(sortedNums)):
        if sortedNums[i] in d:
            continue
        d[sortedNums[i]] = i
    print(d)

    for i in range(len(nums)):
        smaller[i] = d[nums[i]]
    return smaller
    
print(smallerNumbersThanCurrent([6,5,4,8,4]))

## 6 5 4 8 4
## 4 4 5 6 8  Sorted

#Index 0 = 0 always, after = 1 or index
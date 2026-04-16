def test(nums):
    max = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            if max < count:
                max = count
            count = 0
    if max < count:
        return count
    return max

print(test([1,1,1,0,1,1,1,1,1,1]))

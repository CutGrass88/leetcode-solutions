def test(nums, target):
    n = len(nums)
    seen = {}

    for i in range(n):
        needed = target - nums[i]
        
        if needed in seen:
            return [seen[needed], i]
        seen[nums[i]] = i

print(test([2,7,11,15], 9))
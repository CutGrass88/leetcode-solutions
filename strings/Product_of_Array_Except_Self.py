def productExceptSelf(nums):
    before = [1] * len(nums)
    after = [1] * len(nums)

    for i in range(1,len(nums)):
        before[i] *= before[i-1] * nums[i-1]

    for j in range(len(nums)-2,-1,-1):
        after[j] *= after[j+1] * nums[j+1]

    for k in range(len(nums)):
        before[k] *= after[k]
    return before
        

productExceptSelf([2,3,4,5])

# [2,3,4,5]
# []
def test(nums):
    n = len(nums)//2
    ans = [0] * (n*2)
    for i in range(n):
        ans[i*2] = nums[i]
        ans[i*2 + 1] = nums[i+n]
    return ans
print(test([1,3,5,2,4,6]))
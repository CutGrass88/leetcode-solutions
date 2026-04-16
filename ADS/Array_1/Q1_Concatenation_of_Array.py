def test(nums):
    ans = []
    for i in range(len(nums)*2):
        ans.append(nums[i%len(nums)])
    return ans

print(test([1,2,1]))
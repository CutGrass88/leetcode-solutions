def findDisappearedNumbers(nums):
    x = set(nums)

    missing = []
    for j in range(1, len(nums)+1):
        if j not in x:
            missing.append(j)
    return missing
    
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
def findDisappearedNumbers(nums):
    x = set(nums) # Use set for very fast lookup

    missing = []
    for j in range(1, len(nums)+1): # All numbers to n
        if j not in x: # Membership check
            missing.append(j)
    return missing
    
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
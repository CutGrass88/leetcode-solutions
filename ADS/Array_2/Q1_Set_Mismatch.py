def findErrorNums(nums):
    d = {i+1: 0 for i in range(len(nums))}
    for item in nums:
        d[item] += 1 #Count occurences
    double = 0
    missing = 0
    for key in d.keys(): #Check double and find missing
        if d[key] == 0:
            missing = key
        if d[key] == 2:
            double = key
    return [double, missing]

    
        
print(findErrorNums([1,2,2,4]))
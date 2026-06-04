def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    while True:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if high-low <= 0:
            if target > nums[mid]:
                return mid+1
            else:
                if mid <= 0:
                    return 0
                return mid
            
        if nums[mid] < target:
            low = mid+1
        else:
            if mid-1 < 0:
                high = mid
            else:
                high = mid-1

        
print(f"Result: {searchInsert([1,3], 2)}")


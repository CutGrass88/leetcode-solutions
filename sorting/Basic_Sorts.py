def insertionSort(nums):
    
    for i in range(1, len(nums)):
        temp = nums[i] 
        count = 0
        for j in range(i-1,-1,-1):
            if temp < nums[j]:
                count += 1
            else:
                break
        insert = i-count

        for j in range(i, insert, -1):
            nums[j] = nums[j-1]
        nums[insert] = temp
    return nums

def selectionSort(nums):
    for i in range(len(nums)):
        smallest = nums[i]
        smallestIndex = i
        for j in range(i, len(nums)):
            if smallest > nums[j]:
                smallest = nums[j]
                smallestIndex = j
        temp = nums[i]
        nums[i] = smallest
        nums[smallestIndex] = temp
    return nums

def quickSort(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    pivot = nums[-1] #last number is the pivot
    i = -1

    for j in range(len(nums)-1):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i] # swap
    nums[i+1], nums[-1] = nums[-1], nums[i+1] # swap pivot
    left = nums[:i+1] # left half
    right = nums[i+2:] # right half
    
    sortedLeft = quickSort(left)
    sortedRight = quickSort(right)

    return sortedLeft + [pivot] + sortedRight
        
        
nums = [5,3,2,6,1,4]
print(quickSort(nums))

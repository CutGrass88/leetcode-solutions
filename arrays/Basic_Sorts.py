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

print(selectionSort([5,3,2,6,1]))

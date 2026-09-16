def increasingTriplet(nums):
        smallest = float("inf")
        secondSmallest = float("inf")

        for i in range(len(nums)):
            if nums[i] <= smallest:
                smallest = nums[i]
            elif nums[i] <= secondSmallest:
                secondSmallest = nums[i]
            else:
                return True
        return False

print(increasingTriplet([5,6,1,2,3]))
#[1,2,3]
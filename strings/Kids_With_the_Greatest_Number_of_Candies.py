def kidsWithCandies(candies, extraCandies: int):
    maxCandy = max(candies)
    result = [False] * len(candies)
    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxCandy:
            result[i] = True
    return result

print(kidsWithCandies([2,3,5,1,3],3))
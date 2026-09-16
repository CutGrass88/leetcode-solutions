def canPlaceFlowers(flowerbed, n: int):
    canPlace = 0
    if n == 0:
        return True
    for i in range(len(flowerbed)):
        if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0) and flowerbed[i] == 0:
            canPlace += 1
            flowerbed[i] = 1
            if canPlace == n:
                return True
    return False


print(canPlaceFlowers([1,0,1,0,1,0,1], 0))


# [0, 1, 1, 0, 0, 0, 1, 0, 0]
def dailyTemperatures(temperatues):
    ans = [0] * len(temperatues)

    for i in range(0,len(temperatues)-1):
        for j in range(i, len(temperatues)):
            if i == j:
                continue
            if temperatues[i] < temperatues[j]:
                ans[i] = j - i
                break
    return ans

print(dailyTemperatures([30,60,50,90]))
# [30, 60, 50, 90]
# [1, 2, 1, 0]



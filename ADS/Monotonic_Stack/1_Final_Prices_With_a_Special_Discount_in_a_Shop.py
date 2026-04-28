def finalPrices(prices):
    answer = list(prices)
    stack = [] # indices of items needing discount
    for i in range(len(prices)):
        while stack and prices[i] <= prices[stack[-1]]:
            oldIndex = stack.pop()
            answer[oldIndex] = prices[oldIndex] - prices[i]
        stack.append(i)
    return answer
print(finalPrices([8,4,6,2,3]))





#Input: prices = [8,4,6,2,3]
#Output: [4,2,4,2,3]
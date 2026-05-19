def dailyTemperatures(temperatures):
    stack = []
    ans = [0] * len(temperatures)

    for i in range(len(temperatures)):
        if not stack:
            stack.append(i)
            continue
        while stack and temperatures[stack[-1]] < temperatures[i]:
            insertIndex = stack.pop()
            ans[insertIndex] = i - insertIndex
        stack.append(i)
    return ans

print(dailyTemperatures([30,60,50,90]))
# [30, 60, 50, 90]
# [1, 2, 1, 0]

#Think of a stack that maintains order via push and pops
# push 30 index stack=[0], 60 is greater so pop 30 and at index of stack.pop = 60 index
# 0:30 see 60 at 1 stack[1] ans = 1...
#i=2 = 50 push 50 stack [1,2]
#see 90


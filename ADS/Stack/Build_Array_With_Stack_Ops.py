def buildArray(target, n):
    stack = []
    operations = []
    targetSet = set(target)
    for i in range(1, n+1):
        if stack == target:#if they equal stop
            return operations

        if not stack: #if stack empty push
            stack.append(i)
            operations.append("Push")
            continue

        if stack[-1] not in targetSet:#last element not in target pop it
            stack.pop()
            operations.append("Pop")

        stack.append(i)
        operations.append("Push")
    return operations

print(buildArray([1], 2))

            

# target = [1,3] n = 3
# 1 push as stack empty
# does 1 exist in target? if yes continue else pop
# 2 push and repeat logic if in target cont else pop
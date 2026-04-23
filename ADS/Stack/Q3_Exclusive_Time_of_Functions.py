def exclusiveTime(n, logs):
    stack = []
    runningTime = [0] * n
    prevTime = 0
    for i in range(len(logs)):
        log = logs[i]
        params = log.split(":") # (id : start/end : timestamp)
        
        id = int(params[0])
        status = params[1]
        timestamp = int(params[2])

        if status == "start":
            if stack:
                runningTime[stack[-1]] += timestamp - prevTime
            stack.append(id)
            prevTime = timestamp
        elif status == "end":
            runningTime[stack.pop()] += timestamp - prevTime + 1
            prevTime = timestamp + 1
    return runningTime

print(exclusiveTime(2,["0:start:0", "1:start:2", "1:end:5", "0:end:6"]))

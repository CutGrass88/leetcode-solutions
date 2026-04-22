def evalRPN(tokens):
    stack = []
    for token in tokens:
        match token:
            case "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            case "-":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(left - right)
            case "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            case "/":
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(int(left / right))
            case _:
                stack.append(token)
    return int(stack[0])

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


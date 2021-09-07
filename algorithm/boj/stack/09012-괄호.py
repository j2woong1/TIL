for _ in range(0, int(input())):
    stack = []
    parenthesis = list(input())
    for i in parenthesis:
        stack.append(i)
        if len(stack) >= 2:
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

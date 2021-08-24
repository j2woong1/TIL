for tc in range(1, 11):
    N = int(input())
    arr = input()
    stack = []
    ans = []

    for i in range(N):
        if arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ')':
            while stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        elif arr[i] == '+':
            if len(stack) == 0 or (stack[-1] != '*' and stack[-1] != '+'):
                stack.append(arr[i])
            else:
                while stack[-1] == '*' or stack[-1] == '+':
                    ans.append(stack.pop())
                stack.append('+')

        elif arr[i] == '*':
            stack.append(arr[i])
        elif arr[i] != '(' and arr[i] != ')' and arr[i] != '*' and arr[i] != '+':
            ans.append(arr[i])
    for j in range(len(stack)):
        ans.append(stack.pop())

    new = []
    for k in range(len(ans)):
        if ans[k] != '*' and ans[k] != '+' and ans[k] != '(' and ans[k] != ')':
            new.append(ans[k])
        elif ans[k] == '+':
            new.append(int(new.pop()) + int(new.pop()))
        elif ans[k] == '*':
            new.append(int(new.pop()) * int(new.pop()))


    else:
        print("#{} {}".format(tc, new.pop()))
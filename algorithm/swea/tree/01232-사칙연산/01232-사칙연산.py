def cal(num1, sym, num2):
    if sym == '+':
        return num1 + num2
    elif sym == '-':
        return num1 - num2
    elif sym == '*':
        return num1 * num2
    elif sym == '/':
        return num1 / num2


T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 4 for _ in range(N + 1)]
    for i in range(1, N + 1):
        tree = input().split()
        if len(tree) == 4:
            arr[i][0], arr[i][1], arr[i][2] = tree[1], int(tree[2]), int(tree[3])
            arr[arr[i][1]][3] = int(tree[0])
            arr[arr[i][2]][3] = int(tree[0])
        else:
            arr[i][0] = int(tree[1])

    for i in range(N - 1, 0, -2):
        par = arr[i][3]
        arr[par][0] = cal(arr[i][0], arr[par][0], arr[i + 1][0])

    print("#{} {}".format(tc, int(arr[1][0])))

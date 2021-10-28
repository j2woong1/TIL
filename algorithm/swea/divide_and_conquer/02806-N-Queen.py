def nQueen(level):
    global ans
    if level == N:
        ans += 1
        return

    for i in range(N):
        # level-i+n-1 = i - level
        if col[i] or q1[i + level] or q2[level - i + N - 1]:
            continue

        col[i] = 1
        q1[i + level] = 1
        q2[level - i + N - 1] = 1

        nQueen(level + 1)

        col[i] = 0
        q1[i + level] = 0
        q2[level - i + N - 1] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    col, q1, q2 = [0] * (2 * N), [0] * (2 * N), [0] * (2 * N)
    ans = 0
    nQueen(0)

    print('#{} {}'.format(tc, ans))

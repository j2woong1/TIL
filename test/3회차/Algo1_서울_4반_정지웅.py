T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    ai = list(map(int, input().split()))
    arr = []

    for i in range(N - M + 1):
        max_num = 0
        min_num = 10001
        for j in range(M):
            if max_num < ai[i + j]:
                max_num = ai[i + j]
            if min_num > ai[i + j]:
                min_num = ai[i + j]
        arr.append(max_num - min_num)

    print('#{}'.format(tc), end=' ')
    print(*arr)

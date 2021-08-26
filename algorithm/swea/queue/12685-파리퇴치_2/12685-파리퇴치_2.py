t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    flies = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = 0
            for k in range(m):
                for l in range(m):
                    if k == l or k + l == m - 1:
                        total += arr[i + k][j + l]

                if total > flies:
                    total = flies
    print(f'#{tc} {flies}')
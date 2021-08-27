dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]


def concave():
    for i in range(N):
        for j in range(N):
            for k in range(4):  # 상하좌우 4
                cnt = 0
                x, y = i, j
                while 0 <= x < N and 0 <= y < N and arr[x][y] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return "YES"
                    x += dx[k]
                    y += dy[k]
    return "NO"


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    print("#{} {}".format(tc, concave()))

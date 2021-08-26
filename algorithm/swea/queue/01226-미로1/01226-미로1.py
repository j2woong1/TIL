def maze(x, y):
    global ans
    # 상, 우, 하, 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for k in range(4):
        nx = x + dx[k]  # 다음 x
        ny = y + dy[k]  # 다음 y
        if nx in range(N) and ny in range(N):  # 미로 안에서는
            if arr[nx][ny] == 3:  # 도착
                ans = 1
                return ans
            elif arr[nx][ny] == 0:  # 처음 가는 루트
                arr[nx][ny] = 1
                maze(nx, ny)


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(16)]

    ans = 0
    maze(1, 1)
    print(f"#{tc} {ans}")

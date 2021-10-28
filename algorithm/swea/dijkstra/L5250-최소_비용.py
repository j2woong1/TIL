from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    global arr
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                new = 1  # next_add (다음칸으로 더해줄 숫자)
                if H[nx][ny] > H[x][y]:
                    new += H[nx][ny] - H[x][y]
                if arr[nx][ny] > arr[x][y] + new:
                    arr[nx][ny] = arr[x][y] + new  # 갱신
                    q.append((nx, ny))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    arr = [[float('inf') for _ in range(N)] for _ in range(N)]
    arr[0][0] = 0
    bfs(0, 0)  # start x,y

    print("#{} {}".format(tc, arr[N - 1][N - 1]))

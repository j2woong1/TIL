N = int(input())

dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)

start = []
dragon = [list() for _ in range(N)]
visited = [[0] * 101 for _ in range(101)]

for i in range(N):
    x, y, d, g = map(int, input().split())
    curve = 0
    dragon[i].append(d)
    while curve < g:
        for j in dragon[i][::-1]:
            dragon[i].append((j + 1) % 4)
        curve += 1
    visited[y][x] = 1
    for d in dragon[i]:
        y += dy[d]
        x += dx[d]
        visited[y][x] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i + 1][j] and visited[i][j + 1] and visited[i + 1][j + 1]:
            ans += 1
print(ans)

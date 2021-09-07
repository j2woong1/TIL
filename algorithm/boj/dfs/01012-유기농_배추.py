from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

case = int(input())
for _ in range(case):
    M, N, K = map(int, input().split())
    cnt = 0
    graph = []
    for i in range(N):
        graph.append(list(0 for _ in range(M)))

    for i in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1


    def BFS(a, b):
        q = deque()
        q.append((a, b))
        graph[a][b] = '#'
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                    graph[nx][ny] = '#'
                    q.append((nx, ny))
        return


    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                BFS(i, j)
                cnt += 1
    print(cnt)

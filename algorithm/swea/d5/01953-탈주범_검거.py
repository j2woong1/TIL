from collections import deque


def bfs(R, C, L):
    q = deque()
    q.append((R, C, L))
    while q:
        R, C, L = q.popleft()
        if L == L - 1:
            continue
        else:
            if info[R][C] == 1:
                dx = [-1, 0, 1, 0]
                dy = [0, -1, 0, 1]
                for k in range(4):
                    nx = R + dx[k]
                    ny = C + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if k == 0:
                            if info[nx][ny] == 1 or info[nx][ny] == 2 or info[nx][ny] == 5 or info[nx][ny] == 6:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
                        if k == 1:
                            if info[nx][ny] == 1 or info[nx][ny] == 3 or info[nx][ny] == 4 or info[nx][ny] == 5:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
                        if k == 2:
                            if info[nx][ny] == 1 or info[nx][ny] == 2 or info[nx][ny] == 4 or info[nx][ny] == 7:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
                        if k == 3:
                            if info[nx][ny] == 1 or info[nx][ny] == 3 or info[nx][ny] == 6 or info[nx][ny] == 7:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
            elif info[R][C] == 2:
                dx = [-1, 1]
                dy = [0, 0]
                for k in range(2):
                    nx = R + dx[k]
                    ny = C + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if k == 0:
                            if info[nx][ny] == 1 or info[nx][ny] == 2 or info[nx][ny] == 5 or info[nx][ny] == 6:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
                        if k == 1:
                            if info[nx][ny] == 1 or info[nx][ny] == 2 or info[nx][ny] == 4 or info[nx][ny] == 7:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
            elif info[R][C] == 3:
                dx = [0, 0]
                dy = [-1, 1]
                for k in range(2):
                    nx = R + dx[k]
                    ny = C + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if k == 0:
                            if info[nx][ny] == 1 or info[nx][ny] == 3 or info[nx][ny] == 4 or info[nx][ny] == 5:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
                        if k == 1:
                            if info[nx][ny] == 1 or info[nx][ny] == 3 or info[nx][ny] == 6 or info[nx][ny] == 7:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
            elif info[R][C] == 4:
                dx = [-1, 0]
                dy = [0, 1]
                for k in range(2):
                    nx = R + dx[k]
                    ny = C + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if k == 0:
                            if info[nx][ny] == 1 or info[nx][ny] == 2 or info[nx][ny] == 5 or info[nx][ny] == 6:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
                        if k == 1:
                            if info[nx][ny] == 1 or info[nx][ny] == 3 or info[nx][ny] == 6 or info[nx][ny] == 7:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
            elif info[R][C] == 5:
                dx = [1, 0]
                dy = [0, 1]
                for k in range(2):
                    nx = R + dx[k]
                    ny = C + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if k == 0:
                            if info[nx][ny] == 1 or info[nx][ny] == 2 or info[nx][ny] == 4 or info[nx][ny] == 7:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
                        if k == 1:
                            if info[nx][ny] == 1 or info[nx][ny] == 3 or info[nx][ny] == 6 or info[nx][ny] == 7:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
            elif info[R][C] == 6:
                dx = [1, 0]
                dy = [0, -1]
                for k in range(2):
                    nx = R + dx[k]
                    ny = C + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if k == 0:
                            if info[nx][ny] == 1 or info[nx][ny] == 2 or info[nx][ny] == 4 or info[nx][ny] == 7:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
                        if k == 1:
                            if info[nx][ny] == 1 or info[nx][ny] == 3 or info[nx][ny] == 4 or info[nx][ny] == 5:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
            elif info[R][C] == 7:
                dx = [-1, 0]
                dy = [0, -1]
                for k in range(2):
                    nx = R + dx[k]
                    ny = C + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if k == 0:
                            if info[nx][ny] == 1 or info[nx][ny] == 2 or info[nx][ny] == 5 or info[nx][ny] == 6:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))
                        if k == 1:
                            if info[nx][ny] == 1 or info[nx][ny] == 3 or info[nx][ny] == 4 or info[nx][ny] == 5:
                                visited[nx][ny] = 1
                                q.append((nx, ny, L + 1))


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    bfs(R, C, 0)
    ans = 0
    for row in visited:
        ans += sum(row)
    print("#{} {}".format(tc, ans))

##################################################################################

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
pipe = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [1, 2], [2, 3], [0, 3]]


def check(time):
    if time >= L:
        return
    for _ in range(len(q)):
        pos = q.pop(0)
        r = pos[0]
        c = pos[1]
        for i in pipe[info[r][c]]:
            nr = r + dxy[i][0]
            nc = c + dxy[i][1]
            if 0 <= nr <= N - 1 and 0 <= nc <= M - 1 and (i + 2) % 4 in pipe[info[nr][nc]] and (nr, nc) not in visited:
                q.append((nr, nc))
                visited.append((nr, nc))
    time += 1
    check(time)


for t in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    q = [(R, C)]
    visited = [(R, C)]
    check(1)
    print("#%d %d" % (t, len(visited)))

def dfs(v, cnt):
    global ans
    ans = max(ans, cnt)

    for i in nums[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt + 1)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    ans = 0
    for _ in range(M):
        x, y = map(int, input().split())
        nums[x].append(y)
        nums[y].append(x)

    # 정점 1부터 N까지 존재
    for x in range(1, N + 1):
        visited[x] = 1
        dfs(x, 1)
        visited[x] = 0

    print('#%d %d' % (tc, ans))

def work(k, r, used):
    global ans
    if r < ans or r == 0:
        return
    if k == N:
        ans = r
        return
    for i in range(N):
        if used & (1 << i):
            continue
        work(k + 1, r * (nums[k][i]), used | (1 << i))


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    ans = 0
    work(0, 1, 0)
    print('#{0} {1:.6f}'.format(t, ans * 100))

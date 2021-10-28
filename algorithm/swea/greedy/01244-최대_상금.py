T = int(input())


def dfs(exchange):
    global ans
    if exchange == 0:
        ans = max(int(''.join(nums)), ans)
        return

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            if not visited.get((''.join(nums), reward - exchange + 1), 0):
                visited[(''.join(nums), reward - exchange + 1)] = 1
                dfs(exchange - 1)
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, T + 1):
    nums, exchange = input().split()
    nums = list(nums)
    reward = int(exchange)

    ans = 0
    visited = {}
    dfs(reward)
    print("#{} {}".format(tc, ans))

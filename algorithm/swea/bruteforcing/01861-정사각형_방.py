dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    room = [0] * (N * N + 1)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N and nums[i][j] + 1 == nums[nx][ny]:
                    room[nums[i][j]] = 1

    ans = [0, 0]  # 처음 출발해야 하는 방 번호, 최대 몇 개의 방을 이동할 수 있는지
    cnt = 0
    for i in range(1, len(room)):
        cnt += 1
        if not room[i]:
            if ans[1] < cnt:
                ans = [i - cnt + 1, cnt]
            cnt = 0
    print("#{} {} {}".format(tc, ans[0], ans[1]))

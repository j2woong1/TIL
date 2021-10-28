dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def calc(n, x, y):  # n:이동한횟수, x,y:행열 좌표
    global ans

    if n == 7:
        ans.add(''.join(arr))
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            arr[n] = grid[nx][ny]
            calc(n + 1, nx, ny)


T = int(input())
for tc in range(1, T + 1):
    grid = [input().split() for _ in range(4)]
    arr = [''] * 7  # 7개 숫자 채울 리스트
    ans = set()
    for i in range(4):
        for j in range(4):
            calc(0, i, j)

    print("#{} {}".format(tc, len(ans)))

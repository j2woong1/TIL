T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(N)
    # print(arr)

    ans = 0
    for i in range(N):
        mag = 0
        for j in range(N):
            if arr[j][i] == 1:
                mag = 1
            elif arr[j][i] == 2:
                if mag == 1:
                    ans += 1
                    mag = 0

    print(f"#{tc} {ans}")

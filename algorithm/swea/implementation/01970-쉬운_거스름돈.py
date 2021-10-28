T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = [0] * 8

    print("#{}".format(tc))
    for i in range(8):
        ans[i] = N // won[i]
        N %= won[i]
        print(ans[i], end=' ')
    print()

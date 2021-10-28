T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    ans = ''
    while M > 0:
        ans = str(M % 2) + ans
        M //= 2
    print("#%d ON" % t) if ans[-N:] == '1' * N else print("#%d OFF" % t)

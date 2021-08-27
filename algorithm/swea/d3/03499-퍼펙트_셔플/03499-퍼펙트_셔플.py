T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = []
    cards = input().split()
    fir = cards[:(N + 1) // 2]
    sec = cards[(N + 1) // 2:] + ['']
    for i in range(len(fir)):
        ans.append(fir[i])
        ans.append(sec[i])
    print('#%d %s' % (tc, ' '.join(ans).rstrip()))

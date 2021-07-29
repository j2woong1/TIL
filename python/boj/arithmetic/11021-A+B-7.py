T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    ans = A + B
    print('Case #%s: %s'%(i + 1, ans))
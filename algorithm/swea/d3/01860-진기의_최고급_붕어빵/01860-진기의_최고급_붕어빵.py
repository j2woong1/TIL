def Bread():
    total = 0
    cnt = -1
    max_cnt = arr[0]
    for i in range(len(arr)):
        if max_cnt < arr[i]:
            max_cnt = arr[i]
    while True:
        cnt += 1
        if cnt % M == 0 and cnt != 0:
            total += K
        for i in range(len(arr)):
            if cnt == arr[i]:
                if total == 0:
                    return 'Impossible'
                else:
                    total -= 1
        if cnt == max_cnt:
            return 'Possible'


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = Bread()
    print('#{} {}'.format(tc, ans))

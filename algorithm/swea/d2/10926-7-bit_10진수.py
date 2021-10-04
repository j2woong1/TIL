T = int(input())

for tc in range(1, T + 1):
    num = input()
    cnt = 0
    ans = []
    while cnt != 10:
        arr = num[cnt * 7:(cnt + 1) * 7]
        ans.append(int(arr, 2))
        cnt += 1
    print(f'#{tc}', end=' ')
    print(*ans, end=' ')
    print()

############################################

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input()))
    ans = []
    # 7개씩 잘라서 b6 ~ b0로 사용
    dec = 0
    for i in range(70):
        j = 6 - i % 7
        dec += arr[i] * (1 << j)  # j번 비트가 1인 값, 2의 j제곱
        if j == 0:
            ans.append(dec)
            dec = 0
    print(f'#{tc}', *ans)
T = int(input())

dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
       '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a = [input() for i in range(N)]

    tmp1 = ""
    tmp2 = ""
    for i in range(N):
        if '1' in a[i]:
            tmp2 += a[i][::-1]
            break
    for j in range(M):
        if tmp2[j] == '1':
            tmp1 += tmp2[j:j + 56][::-1]
            break

    arr = [tmp1[i:i + 7] for i in range(0, 56, 7)]

    res = []
    for i in arr:
        res.append(dic[i])
    ans = 0
    if ((res[0] + res[2] + res[4] + res[6]) * 3 + res[1] + res[3] + res[5] + res[7]) % 10 == 0:
        ans = sum(res)

    print("#{} {}".format(tc, ans))

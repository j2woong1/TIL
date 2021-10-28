T = int(input())

code = {'112': 0, '122': 1, '221': 2, '114': 3, '231': 4, '132': 5, '411': 6, '213': 7, '312': 8, '211': 9}
hexa = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N세로, M가로
    a = [input()[:M] for i in range(N)]  
    visited = []
    ans = 0

    for i in range(N):
        bin = ''
        for ele in a[i]:
            bin += hexa[ele]

        if '1' in bin:
            bin = bin.rstrip('0')
            res = []
            f, s, t = 0, 0, 0
            for j in range(len(bin) - 1, -1, -1):
                if s == 0 and t == 0 and bin[j] == '1':
                    f += 1
                elif f != 0 and t == 0 and bin[j] == '0':
                    s += 1
                elif f != 0 and s != 0 and bin[j] == '1':
                    t += 1
                elif t != 0 and bin[j] == '0':
                    minn = min(f, s, t)
                    tmp = str(f // minn) + str(s // minn) + str(t // minn)
                    res.append(code[tmp])
                    f, s, t = 0, 0, 0  # 초기화
                if len(res) == 8:
                    if res not in visited:
                        visited.append(res)  # 방문체크
                        if ((res[1] + res[3] + res[5] + res[7]) * 3 + res[0] + res[2] + res[4] + res[6]) % 10 == 0:
                            ans += sum(res)
                    res = []  # 초기화

    print("#{} {}".format(tc, ans))

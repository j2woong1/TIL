def mono(num):
    num = str(num)
    for x in range(len(num) - 1):  # 앞 숫자 크면 False
        if num[x] > num[x + 1]:
            return False
    return True


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = -1  # 없으면 -1

    for i in range(N):
        for j in range(i + 1, N):
            total = arr[i] * arr[j]
            if mono(total) and total > ans:  # 단조, 최대값 체크
                ans = total

    print(f"#{t} {ans}")

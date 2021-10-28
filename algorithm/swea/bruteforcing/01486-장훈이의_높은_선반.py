from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())  # N:직원수, B:선반높이
    H = list(map(int, input().split()))

    ans = []
    for i in range(1, N + 1):
        tower = combinations(H, i)  # i개(1~N) 뽑는 경우의수
        for j in tower:
            tmp = sum(j)
            if tmp >= B:
                ans.append(tmp)

    print("#{} {}".format(tc, min(ans) - B))

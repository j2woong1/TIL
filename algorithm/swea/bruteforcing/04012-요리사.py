# 음식 조합
def perm(idx, k):
    global res
    # n개의 조합이 완성됐으면,
    if idx == n:
        arr2 = [i for i in range(N) if visited[i]]
        # arr2 : n개를 뽑고 남은 나머지 n개의 list
        s1 = s2 = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                s1 += S[arr[i]][arr[j]] + S[arr[j]][arr[i]]
                s2 += S[arr2[i]][arr2[j]] + S[arr2[j]][arr2[i]]
        # food1, food2의 시너지의 합 계산
        x = abs(s1 - s2)
        # x : 시너지의 합의 차
        if x < res:
            res = x
            # 최솟값이면 result에 저장
        return
    # k 부터 N 까지 => k부터 하지 않으면 시간초과 발생!
    # k 앞부분은 이미 탐색했으므로 다시 돌 필요가 없다.
    for i in range(k, N):
        if visited[i]:
            arr[idx] = i
            visited[i] = 0
            perm(idx + 1, i + 1)
            visited[i] = 1


ans = []
for tc in range(1, 1 + int(input())):
    N = int(input())
    n = N // 2
    S = [list(map(int, input().split())) for _ in range(N)]
    visited = [1] * N
    # 초기값을 1로 두고 방문했으면 0으로 바꿈
    res = 987654321
    arr = [0] * n
    perm(0, 0)

    ans.append(('#{} {}'.format(tc, res)))

print('\n'.join(ans))

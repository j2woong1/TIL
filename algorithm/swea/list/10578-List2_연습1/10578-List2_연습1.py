"""
# List2_연습1
NxN 배열에서 각 요소에 대해서, 그 요소와 이웃한 요소와의 차의 절대값에 대한 합을 구한 후, 총 합

테스트케이스 t,
다음 줄부터 테스트케이스 별로 첫 줄에 N,
다음 줄부터 N개의 줄에 공백으로 구분된 1이상 99이하의 정수가 N개씩 제공

#과 테스트케이스 번호, 빈칸에 이어 모든 원소에 대한 이웃한 숫자와의 차의 절대값에 대한 총 합을 출력
"""

# t = int(input())
#
# for tc in range(1, t+1):
#     n = int(input())
#     arr = []
#
#     for i in range(n):
#         num = list(map(int, input().split()))
#         arr.append([num[0]] + num + [num[len(num)-1]])
#     arr = [arr[0]] + arr + [arr[len(arr)-1]]
#     ans = 0
#
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             up = abs(arr[i][j] - arr[i-1][j])
#             down = abs(arr[i][j] - arr[i+1][j])
#             left = abs(arr[i][j] - arr[i][j-1])
#             right = abs(arr[i][j] - arr[i][j+1])
#             total = up + down + left + right
#             ans += total
#
#     print(f'#{tc} {ans}')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0  # 모든 원소에 대해 주변 원소와의 절대값의 합

    for i in range(n):
        for j in range(n):
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj  # i, j의 주변 ni, nj
                if 0 <= ni < n and 0 <= nj < n:
                    ans += abs(arr[i][j] - arr[ni][nj])

    print(f'#{tc} {ans}')

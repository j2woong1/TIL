"""
# 가로 세로의 최대합
N x N 배열에서 한 칸을 선택했을 때 그 칸을 포함하는 가로 행과 세로 열에 포함된 값들의 총합이 최대가 되는 경우

첫 줄에 테스트케이스 수가 주어진다.
다음으로 배열의 크기 N(1<= N <= 30)이 주어진다.
다음 N개의 줄에 공백으로 구분된 N개의 정수 aij 값이 주어진다.

'#'과 케이스 번호를 출력하고 총합이 최대가 되는 값을 출력
"""

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    aij = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N):
        for j in range(N):
            tmp_sum = 0
            for k in range(N):
                tmp_sum += (aij[i][k] + aij[k][j])
            tmp_sum -= aij[i][j]

            if tmp_sum > max_sum:
                max_sum = tmp_sum

    print(f'#{tc} {max_sum}')


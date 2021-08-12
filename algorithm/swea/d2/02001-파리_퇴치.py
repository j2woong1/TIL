"""
# 파리 퇴치
n x n 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수
m x m 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 n 과 m 이 주어지고,
다음 n 줄에 걸쳐 n x n 배열이 주어진다.

출력의 각 줄은 '# t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력
"""

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]  # n X n
    # total = [[0] * m for _ in range(m)] # m X m (blank)

    # # m의 왼쪽 구석 좌표 기준, n-m까지 가능한
    # for k in range(m):
    #     for l in range(m):
    #         for i in range(0, n-m+1):
    #             for j in range(0, n-m+1):
    #                 total[k][l] = arr[i+k][j+l]

    flies = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = 0
            for k in range(i, i + m):
                for l in range(j, j + m):
                    total += arr[k][l]
            if total > flies:
                flies = total

    print(f"#{tc} {flies}")

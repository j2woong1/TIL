"""
# 색칠하기
인덱스가 있는 10x10 격자에 빨간색과 파란색
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때,
칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램

첫 줄에 테스트 케이스 개수 T가 주어진다.
다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다.
다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다.

각 줄마다 "#t" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력
"""

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        # 각각의 위치에 해당하는 색깔을 배열에 더함
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color

    cnt = 0
    for i in range(10):
        for j in range(10):
            # 1, 2 색깔이 합쳐져 3
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')

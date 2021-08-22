"""
# 달팽이 숫자
달팽이는 1부터 N*N 까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N 크기의 달팽이를 출력하시오.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

각 줄은 '# tc'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력
"""


def get_snail(n):
    # 우하좌상 순으로 규칙적으로 진행됨
    # 이에 따른 델타 좌표 dx, dy
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 달팽이 숫자 저장할 리스트
    snail = [[0] * n for _ in range(n)]
    num = 1
    # 델타 좌표 활용하기 위한 변수 case
    case = 0
    x, y = 0, -1
    # n이 3일 때 3 2 2 1 1 이런식으로 진행
    # 첫 번째 경우만 따로 처리
    for _ in range(n):
        x += dx[case]
        y += dy[case]
        snail[x][y] = num
        num += 1
    # 반복되는 경우 처리
    for i in range(n - 1, 0, -1):
        for _ in range(2):
            case += 1
            for _ in range(i):
                x += dx[case % 4]
                y += dy[case % 4]
                snail[x][y] = num
                num += 1
    return snail


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    print(f'#{tc}')
    result = get_snail(n)
    for nums in result:
        print(*nums)

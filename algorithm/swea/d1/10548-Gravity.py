"""
Gravity
오른쪽 90도 회전 : 중력의 영향 낙하
낙차가 가장 큰 상자를 구하여 그 낙차를 리턴

중력은 회전이 완료된 후
상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
방의 가로, 세로 길이 100
즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다.
"""

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    max_fall = 0

    for i in range(0, len(boxes) - 1):
        bigger = 0
        for j in range(i + 1, len(boxes)):
            if boxes[j] >= boxes[i]:
                bigger += 1

        i_max_fall = len(boxes) - i - 1 - bigger
        if i_max_fall > max_fall:
            max_fall = i_max_fall

    print(f'#{t} {max_fall}')

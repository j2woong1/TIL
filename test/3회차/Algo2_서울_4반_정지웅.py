T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    point = input().split()

    row = int(point[3]) - int(point[1]) + 1
    column = int(point[2]) - int(point[0]) + 1
    new = [list(map(int, input().split())) for _ in range(N)]

    area = row * column
    cur = 0
    height = 0
    for i in range(int(point[0]), int(point[2]) + 1):
        for j in range(int(point[1]), int(point[3]) + 1):
            cur += new[i][j]
    height = cur // area
    cost = 0

    for i in range(int(point[0]), int(point[2]) + 1):
        for j in range(int(point[1]), int(point[3]) + 1):
            cost += abs(height - new[i][j])

    print('#{} {} {}'.format(tc, height, cost))

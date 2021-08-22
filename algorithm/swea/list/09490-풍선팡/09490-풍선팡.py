"""
# 풍선팡
어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임
NxM개의 풍선에 들어있는 종이 꽃가루 개수 A가 주어지면,
한 개의 풍선을 선택했을 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력

첫 줄에 테스트케이스 수 t
다음 줄부터 테스트케이스 별로 첫 줄에 N과 M
이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수

#과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력
"""

t = int(input())
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for tc in range(1, t + 1):
    m, n = map(int, input().split())

    ball = [[0] + list(map(int, input().split())) + [0] for _ in range(m)]
    ball.insert(0, [0] * (n + 2))
    ball.append([0] * (n + 2))

    pollen = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            point = ball[i][j]
            s = point
            for k in range(4):
                p = 0
                temp_m = i + dr[k]
                temp_n = j + dc[k]
                position = ball[temp_m][temp_n]

                while position != 0:
                    if p >= point:
                        break
                    s += position
                    p += 1
                    temp_m += dr[k]
                    temp_n += dc[k]
                    position = ball[temp_m][temp_n]

                if pollen < s:
                    pollen = s

    print(f'#{tc} {pollen}')

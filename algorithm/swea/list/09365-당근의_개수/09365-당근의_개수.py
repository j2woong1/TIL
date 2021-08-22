"""
가장 많은 당근이 나온 구역은 몇 번 째 인지와 그 구역의 당근 개수를 출력
당근의 수가 같은 구역이 있을 때는 먼저 수확한 구역의 순서
첫 줄에 테스트케이스 개수 t
구역의 수 n
각 구역의 당근의 개수 C
# 테스트케이스번호, 구역의 순서와 당근의 개수를 빈칸을 두고 출력
"""

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    c = list(map(int, input().split()))

    section = 0
    carrots = c[0]

    for sec, car in enumerate(c):
        if car > carrots:
            carrots = car
            section = sec
    print(f'#{tc} {section + 1} {carrots}')

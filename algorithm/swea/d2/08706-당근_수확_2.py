"""
번호가 붙은 밭에서 모든 당근을 0번 구역으로 옮길 때, 일꾼이 이동한 총 거리를 알아내는 프로그램
테스트케이스 t,
다음 줄부터 테스트케이스 별로 첫 줄에 N과 수레에 실을 수 있는 용량 M,
다음줄에 구역별로 10개 이하의 당근 개수
"""

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    area = list(map(int, input().split()))

    dist = 0
    carrot = 0
    i = 0

    while i < n:
        if area[i] >= m - carrot:
            area[i] -= m - carrot
            carrot = 0
            dist += (i + 1) * 2
        else:
            carrot += area[i]
            i += 1
            dist += 1
    dist += n
    print(f'#{tc} {dist}')

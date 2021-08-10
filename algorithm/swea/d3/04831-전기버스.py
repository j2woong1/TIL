"""
종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력
충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력
"""

t = int(input())

for tc in range(1, t + 1):
    k, n, m = map(int, input().split())
    charge = [0] + list(map(int, input().split())) + [n]
    last = 0
    ans = 0
    for i in range(1, m + 2):
        if charge[i] - charge[i - 1] > k:  # 운행 불가 간격인지 확인
            ans = 0
            break
        if charge[i] > last + k:
            last = charge[i - 1]
            ans += 1
    print(f'{tc} {ans}')

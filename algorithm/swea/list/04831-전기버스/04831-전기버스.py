"""
종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력
충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력
"""

T = int(input())
for t in range(1, T + 1):
    k, n, m = map(int, input().split())
    stations = list(map(int, input().split()))
    result = 0
    start = 0
    impossible = False
    while True:
        end = start + k
        # 끝에 도달하거나 불가능이면 탈출
        if end >= n or impossible:
            break
        # 뒤부터 탐색하여 K범위 내 가장 먼 충전기와 만나면 진행, 못만나면 불가능
        for i in range(end, start - 1, -1):
            # 간 곳이 start와 같으면 충전기가 없는 것이다. 불가능으로 판별
            if i == start:
                impossible = True
                break
            # 간 곳이 충전기이면 진행
            if i in stations:
                start = i
                result += 1
                break

    if impossible:
        print(f'#{t} 0')
    else:
        print(f'#{t} {result}')

"""
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력
"""

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))
    # 1
    max_num = sum(ai[0:m])
    min_num = sum(ai[0:m])
    # 2
    for i in range(0, n - m + 1):
        temp = sum(ai[i:i + m])
        if min_num >= temp:
            min_num = temp
        if max_num <= temp:
            max_num = temp
    ans = max_num - min_num
    print(f'#{tc} {ans}')

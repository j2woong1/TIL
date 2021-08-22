"""
# 특별한 정렬
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=t<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다.

각 줄마다 "#t" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력
"""

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    # 정렬할 리스트
    ai = list(map(int, input().split()))

    # 기준으로 잡을 값 idx와 인덱스와 접근할 때 사용할 값 j
    idx = 0
    j = 0
    while j < n:

        # 리스트 전체를 돌며 기준 값을 이용한 최소, 최대 값을 구한다.
        for i in range(j, n):
            # 리스트 인덱스가 홀수 일때는 최소값이 들어간다.
            if j % 2 == 1:
                if ai[idx] > ai[i]:
                    idx = i
            # 리스트 인덱스가 짝수 일때는 최대값이 들어간다.
            else:
                if ai[idx] < ai[i]:
                    idx = i

        ai[j], ai[idx] = ai[idx], ai[j]

        # 다음 인덱스에 넣을 값을 찾아야하므로 j를 1증가시킨다.
        j += 1
        # idx의 위치도 다음 인덱스의 첫값이 되도록 바꾼다.
        idx = j

    result = ai[:10]

    print("#{}".format(tc), *result)
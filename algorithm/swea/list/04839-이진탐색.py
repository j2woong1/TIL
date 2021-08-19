"""
# 이진탐색
첫 줄에 테스트 케이스 개수 t
테스트 케이스 별로 책의 전체 쪽 수 P, Pa, B가 찾을 쪽 번호 Pa, Pb

각 줄마다 "#t" (T는 테스트 케이스 번호)를 출력한 뒤, Pa, Pb, 0 중 하나를 출력
"""

t = int(input())

for tc in range(1, t + 1):
    arr = [i for i in range(1, 13)]  # 1 ~ 12
    length = len(arr)
    n, k = map(int, input().split())  # num / sum

    cnt = 0
    for i in range(1 << length):
        sub = []
        for j in range(length):
            if i & (1 << j):
                sub.append(arr[j])

        if len(sub) == n:
            if sum(sub) == k:
                cnt += 1
                # print()

    print(f"#{tc} {cnt}")
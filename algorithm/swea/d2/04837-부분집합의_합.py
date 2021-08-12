"""
1부터 12까지의 숫자를 원소로 가진 집합 A
집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램

첫 줄에 테스트 케이스 개수 t
부분집합 원소의 수 N과 부분 집합의 합 K가 여백

각 줄마다 "#t" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력
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

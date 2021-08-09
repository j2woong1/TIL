"""
주어진 N 길이의 숫자열을 오름차순으로 정렬
"""

import sys

T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    print(f'#{tc}', end=' ')
    for x in A:
        print(x, end=' ')
    print()

import sys

input = sys.stdin.readline


def binary_search(target, lst):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == lst[mid]:
            return 1
        elif target > lst[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
ar = list(map(int, input().split()))

for i in ar:
    print(binary_search(i, A))

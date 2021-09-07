import sys

input = sys.stdin.readline

N = int(input())
card_lst = list(map(int, input().split()))
M = int(input())
num_lst = list(map(int, input().split()))
arr = {}

for card in card_lst:
    if card in arr:
        arr[card] += 1
    else:
        arr[card] = 1

for num in num_lst:
    if num in arr:
        print(arr[num], end=' ')
    else:
        print(0, end=' ')
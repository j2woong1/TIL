# 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복

t = int(input())

for _ in range(t):
    cnt, word = input().split()
    for i in word:
        print(i * int(cnt), end='')
    print()
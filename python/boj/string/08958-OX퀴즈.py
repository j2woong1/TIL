# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수

n = int(input())

for _ in range(n):
    a = input()
    score = 0
    total = 0
    for i in a:
        if i == 'O':
            score += 1
        else:
            score = 0
        total += score
    print(total)
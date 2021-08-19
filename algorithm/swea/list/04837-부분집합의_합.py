"""
1부터 12까지의 숫자를 원소로 가진 집합 A
집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램

첫 줄에 테스트 케이스 개수 t
부분집합 원소의 수 N과 부분 집합의 합 K가 여백

각 줄마다 "#t" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력
"""

t = int(input())
for tc in range(1, t + 1):
    P, A, B = map(int, input().split())
    cnt_a = 0
    cnt_b = 0
    l = 1
    r = P
    while 1:
        c = int((l + r) / 2)
        cnt_a += 1
        if c == A:
            break
        elif c <= A:
            l = c
        else:
            r = c
    l = 1
    r = P
    while 1:
        c = int((l + r) / 2)
        cnt_b += 1
        if c == B:
            break
        elif c <= B:
            l = c
        else:
            r = c

    if cnt_a == cnt_b:
        print("#%d %d" % (tc, 0))
    elif cnt_a > cnt_b:
        print("#%d %c" % (tc, 'B'))
    else:
        print("#%d %c" % (tc, 'A'))


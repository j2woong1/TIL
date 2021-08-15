"""
# 이진탐색
첫 줄에 테스트 케이스 개수 t
테스트 케이스 별로 책의 전체 쪽 수 P, Pa, B가 찾을 쪽 번호 Pa, Pb

각 줄마다 "#t" (T는 테스트 케이스 번호)를 출력한 뒤, Pa, Pb, 0 중 하나를 출력
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

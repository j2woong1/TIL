"""
# 쇠막대기 자르기
"""

T = int(input())

for tc in range(1, T + 1):
    iron = input()
    stack, ans = 0, 0

    for i in range(len(iron)):
        if iron[i] == '(':
            if iron[i + 1] == ')':
                ans += stack
            else:
                stack += 1
        else:
            if iron[i - 1] == '(':
                continue
            else:
                stack -= 1
                ans += 1
    print(f'#{tc} {ans}')

x = 0
while x < 10:
    n = int(input())
    text = input()
    s = []
    postfix = ''

    # 후위표현식
    for i in range(n):
        if text[i].isdigit():           # 숫자일 떄
            postfix += text[i]

        else:                           # 연산일 때
            if text[i] == '+':          # +
                while len(s) > 0:
                    postfix += s.pop()
                s.append(text[i])       # 현재 연산을 추가

            elif text[i] == '*':        # *
                s.append(text[i])       # stack 추가

    while len(s) > 0:                   # for 종료 후 모든 연산
        postfix += s.pop()

    # print(postfix)

    # 계산
    cal_s = []
    for i in range(n):
        if postfix[i].isdigit():        # 숫자일 떄
            cal_s.append(postfix[i])    # stack 추가

        else:                           # 연산자일 떄
            num1 = int(cal_s.pop(-2))   # 최근 2번째
            num2 = int(cal_s.pop(-1))   # 최근 1번째

            if postfix[i] == '*':       # * 연산 후 stack 추가
                cal_s.append(num1*num2)
            elif postfix[i] == '+':     # + 연산 후 stack 추가
                cal_s.append(num1+num2)

    print('#{} {}'.format(x+1, cal_s.pop()))
    x += 1